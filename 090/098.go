package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"math"
	"sort"
	"strconv"
	"strings"
	"sync"
)

const (
	numAnagramRoutines = 4
)

type Anagram struct {
	word1 string
	word2 string
}

type Mask []string

func NewMask(s string) Mask {
	return strings.Split(s, "")
}
func (m Mask) GetMask() string {
	return strings.Join(m, "")
}

type Result struct {
	words    Anagram
	replaced Anagram
}

func loadWords(filename string, output chan string) {
	defer close(output)
	file, err := ioutil.ReadFile("words.txt")
	if err != nil {
		return
	}
	data := bytes.Split(file, []byte{'\n'})
	for d := range data {
		output <- string(data[d])
	}
}

func getAnagrams(words chan string, output chan Anagram) {
	data := make(map[string][]string)

	for word := range words {
		word_parts := strings.Split(word, "")
		sort.Strings(word_parts)
		key := strings.Join(word_parts, "")

		for other_word := range data[key] {
			output <- Anagram{word, data[key][other_word]}
		}
		data[key] = append(data[key], word)
	}
	close(output)
}

func resultWatcher() chan Result {
	result := make(chan Result)
	highest_found := 0
	go func() {
		for r := range result {
			i, _ := strconv.Atoi(r.replaced.word1)
			j, _ := strconv.Atoi(r.replaced.word2)
			if i > highest_found {
				highest_found = i
				fmt.Println("New Hightest Found:", i, r)
			}
			if j > highest_found {
				highest_found = j
				fmt.Println("New Hightest Found:", j, r)
			}
		}
	}()
	return result
}

func anagramFinder(anagrams chan Anagram, results chan Result, wg *sync.WaitGroup) {
	for anagram := range anagrams {
		findPowerPairs(anagram, results)
	}
	wg.Done()
}

func findPowerPairs(anagram Anagram, results chan Result) {
	masks := generatePowers(len(anagram.word1))

	for m := range masks {
		mask := NewMask(strconv.Itoa(m))
		replaced := replace(anagram, mask)
		j, _ := strconv.Atoi(replaced.word2)
		if isSquare(j) && strings.Split(replaced.word2, "")[0] != "0" {
			results <- Result{anagram, replaced}
		}
	}
}

func generatePowers(length int) chan int {
	output := make(chan int)
	go func() {
		start := int(math.Ceil(math.Sqrt(math.Pow(10.0, float64(length-1)))))
		end := int(math.Sqrt(math.Pow(10.0, float64(length)) - 1))
		for i := start; i <= end; i++ {
			output <- i * i
		}
		close(output)
	}()
	return output
}

func isSquare(i int) bool {
	return math.Pow(math.Floor(math.Sqrt(float64(i))), 2) == float64(i)
}

func replace(anagram Anagram, mask Mask) Anagram {
	word_array := strings.Split(anagram.word1, "")
	word_array_2 := strings.Split(anagram.word2, "")
	past_replacements := make(map[string]string)
	mask_assingments := make(map[string]string)

	for i := 0; i < len(mask); i++ {
		this_letter := word_array[i]
		this_mask := mask[i]
		if past_replacements[this_letter] != "" && past_replacements[this_letter] != mask[i] {
			return Anagram{"0", "0"}
		}
		if mask_assingments[this_mask] != "" && mask_assingments[this_mask] != this_letter {
			return Anagram{"0", "0"}
		}
		past_replacements[this_letter] = mask[i]
		mask_assingments[mask[i]] = this_letter
		word_array[i] = mask[i]
	}

	for i := 0; i < len(word_array_2); i++ {
		word_array_2[i] = past_replacements[word_array_2[i]]
	}

	return Anagram{strings.Join(word_array, ""), strings.Join(word_array_2, "")}
}

func main() {
	words := make(chan string)
	go loadWords("words.txt", words)

	anagrams := make(chan Anagram)
	go getAnagrams(words, anagrams)

	var wg sync.WaitGroup

	results := resultWatcher()

	for i := 0; i < numAnagramRoutines; i++ {
		wg.Add(1)
		go anagramFinder(anagrams, results, &wg)
	}
	wg.Wait()
}

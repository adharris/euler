package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Exponent struct {
	base  int
	power int
	line  int
}

func (e Exponent) String() string {
	return fmt.Sprintf("%v^%v (line %v)", e.base, e.power, e.line)
}

func (e Exponent) Print() {
	fmt.Println(e.String())
}

func (e Exponent) GreaterThan(o Exponent) bool {
	return float64(e.power)*math.Log(float64(e.base)) > float64(o.power)*math.Log(float64(o.base))
}

func LoadExponents(filename string) chan Exponent {
	output := make(chan Exponent)
	go func() {
		defer close(output)
		fileReader, _ := os.Open(filename)

		defer fileReader.Close()
		fileBuffer := bufio.NewReader(fileReader)
		line := 0
		for {
			s, err := fileBuffer.ReadString('\n')
			if err != nil {
				break
			}
			line++
			parts := strings.Split(strings.Trim(s, "\r\n"), ",")
			base, _ := strconv.Atoi(parts[0])
			exp, _ := strconv.Atoi(parts[1])
			output <- Exponent{base, exp, line}
		}
	}()
	return output
}

func main() {
	exponents := LoadExponents("base_exp.txt")

	largest_exponent := <-exponents

	for e := range exponents {
		if e.GreaterThan(largest_exponent) {
			fmt.Printf("%v is greater than %v\n", e, largest_exponent)
			largest_exponent = e
		}
	}
	fmt.Println("The max is", largest_exponent)

}

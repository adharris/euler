package main

import (
	"fmt"
	"math"
)

type Box struct {
	blue int64
	red  int64
}

func (b Box) String() string {
	n, d := b.ChanceOfBlue()
	p := float64(n) / float64(d)
	return fmt.Sprintf("Total: %v Blue: %v Red: %v %v%%", b.Size(), b.blue, b.red, p)
}

func (b Box) Size() int64 {
	return b.red + b.blue
}

func (b Box) ChanceOfBlue() (num, denom int64) {
	num = b.blue * (b.blue - 1)
	denom = b.Size() * (b.Size() - 1)
	return
}

func (b Box) Is50PercentBlue() bool {
	num, denom := b.ChanceOfBlue()
	return num*2 == denom
}

func makeClosestBox(size int64) Box {
	var b int64
	s := float64(size)
	b = (int64(math.Sqrt(2*s*s-2*s+1)) + 1) / 2
	return Box{b, size - b}
}

func findBoxAfter(box1, box2 Box) Box {
	ratio := float64(box2.Size()) / float64(box1.Size())
	start := int64(float64(box2.Size()) * ratio)
	for i := start; true; i++ {
		b := makeClosestBox(i)
		if b.Is50PercentBlue() {
			fmt.Printf("Needed %v loops\n", i-start)
			return b
		}
	}
	return box2
}

func main() {
	box1 := Box{15, 6}
	box2 := Box{85, 35}

	var find_size int64 = 1000000000000

	for box2.Size() <= find_size {
		box3 := findBoxAfter(box1, box2)
		fmt.Println(box3)
		box1, box2 = box2, box3
	}
}

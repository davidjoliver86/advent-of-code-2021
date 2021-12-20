package main

import (
	"davidjoliver86/advent-of-code-2021/utils"
	"fmt"
)

// CountIncreases counts and return the number of times that one value is greater than the previous value in a slice of ints.
func CountIncreases(ints []int) int {
	increases := 0
	previous := ints[0]
	for _, current := range ints {
		if current > previous {
			increases += 1
		}
		previous = current
	}
	return increases
}

// ConsolidateAddNextTwo consolidates a sequence of n integers into an n-2 length slice, where each element is itself plus the next two in the original slice.
func ConsolidateAddNextTwo(ints []int) []int {
	consolidated := make([]int, len(ints)-2)
	for i := 0; i < len(consolidated); i++ {
		consolidated[i] = ints[i] + ints[i+1] + ints[i+2]
	}
	return consolidated
}

func FirstStar() int {
	ints := utils.IntsFromFile("../fixtures/day1.txt")
	return CountIncreases(ints)
}

func SecondStar() int {
	ints := utils.IntsFromFile("../fixtures/day1.txt")
	return CountIncreases(ConsolidateAddNextTwo(ints))
}

func main() {
	fmt.Println(FirstStar())
	fmt.Println(SecondStar())
}

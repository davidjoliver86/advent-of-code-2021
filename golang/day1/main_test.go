package main

import (
	"reflect"
	"testing"
)

func TestCountIncreases(t *testing.T) {
	testcase := []int{199, 200, 208, 210, 200, 207, 240, 269, 260, 263}
	actual := CountIncreases(testcase)
	if actual != 7 {
		t.Errorf("Expected 7 increases, got %v", actual)
	}
}

func TestConsolidateAddNextTwo(t *testing.T) {
	testcase := []int{199, 200, 208, 210, 200, 207, 240, 269, 260, 263}
	expected := []int{607, 618, 618, 617, 647, 716, 769, 792}
	actual := ConsolidateAddNextTwo(testcase)
	if !reflect.DeepEqual(expected, actual) {
		t.Errorf("Expected %v, got %v", expected, actual)
	}
}

func TestFirstStar(t *testing.T) {
	actual := FirstStar()
	if actual != 1832 {
		t.Errorf("Expected 1832, got %v", actual)
	}
}

func TestSecondStar(t *testing.T) {
	actual := SecondStar()
	if actual != 1858 {
		t.Errorf("Expected 1858, got %v", actual)
	}
}

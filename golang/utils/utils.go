package utils

import (
	"log"
	"os"
	"strconv"
	"text/scanner"
)

func IntsFromFile(path string) []int {
	fp, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer fp.Close()

	// Initalize scanner
	var s scanner.Scanner
	s.Init(fp)
	s.Mode = scanner.ScanInts

	// Initialize int slice
	ints := make([]int, 0)

	for tok := s.Scan(); tok != scanner.EOF; tok = s.Scan() {
		val, err := strconv.ParseInt(s.TokenText(), 0, 32)
		if err != nil {
			log.Fatalf("not an integer: %v", s.TokenText())
		}
		ints = append(ints, int(val))
	}
	return ints
}

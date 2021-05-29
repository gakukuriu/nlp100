package main

import (
	"fmt"
	"strings"
)

func contains(nums []int, n int) bool {
	for _, v := range nums {
		if v == n {
			return true
		}
	}
	return false
}

func main() {
	s := "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
	words := strings.Split(s, " ")
	numbers := []int{1, 5, 6, 7, 8, 9, 15, 16, 19}
	m := make(map[string]int)

	for i, w := range words {
		runew := []rune(w)
		if contains(numbers, i+1) {
			m[string(runew[0])] = i + 1
		} else {
			m[string(runew[:2])] = i + 1
		}
	}

	fmt.Println(m)
}

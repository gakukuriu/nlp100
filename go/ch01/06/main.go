package main

import (
	"fmt"
)

func union(X map[string]int, Y map[string]int) map[string]int {
	Z := make(map[string]int)

	for k, _ := range X {
		Z[k] = 1
	}
	for k, _ := range Y {
		Z[k] = 1
	}

	return Z
}

func intersection(X map[string]int, Y map[string]int) map[string]int {
	Z := make(map[string]int)

	for k, _ := range X {
		_, ok := Y[k]
		if ok {
			Z[k] = 1
		}
	}

	return Z
}

func difference(X map[string]int, Y map[string]int) map[string]int {
	Z := make(map[string]int)

	for k, _ := range X {
		_, ok := Y[k]
		if !ok {
			Z[k] = 1
		}
	}

	return Z
}

func express(X map[string]int) []string {
	var ws []string
	for k, _ := range X {
		ws = append(ws, k)
	}
	return ws
}

func main() {
	s1 := "paraparaparadise"
	s2 := "paragraph"

	X := Ngram_letters(2, s1)
	Y := Ngram_letters(2, s2)
	setX := make(map[string]int)
	setY := make(map[string]int)

	for _, v := range X {
		setX[v] = 1
	}

	for _, v := range Y {
		setY[v] = 1
	}

	_, seInX := setX["se"]
	_, seInY := setY["se"]

	fmt.Println("union of X and Y: ", express(union(setX, setY)))
	fmt.Println("intersection of X and Y: ", express(intersection(setX, setY)))
	fmt.Println("difference of X and Y: ", express(difference(setX, setY)))
	fmt.Println("se in X?: ", seInX)
	fmt.Println("se in Y?: ", seInY)

}

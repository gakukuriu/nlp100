package main

import (
	"fmt"
)

func main() {
	s1 := "パトカー"
	s2 := "タクシー"
	runes1 := []rune(s1)
	runes2 := []rune(s2)
	var runes3 []rune

	for i := 0; i < len(runes1); i = i + 1 {
		runes3 = append(runes3, runes1[i])
		runes3 = append(runes3, runes2[i])
	}

	fmt.Println(string(runes3))
}

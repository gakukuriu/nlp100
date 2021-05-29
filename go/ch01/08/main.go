package main

import (
	"fmt"
)

func cipher(s string) string {
	runes := []rune(s)
	for i, v := range runes {
		if v >= 'a' && v <= 'z' {
			runes[i] = 219 - v
		}
	}
	return string(runes)
}

func main() {
	s := "I am an NLPer"

	fmt.Println(cipher((s)))

}

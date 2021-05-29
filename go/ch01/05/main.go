package main

import (
	"fmt"
)

func main() {
	s := "I am an NLPer"
	fmt.Println(Ngram_words(2, s))
	fmt.Println(Ngram_letters(2, s))
}

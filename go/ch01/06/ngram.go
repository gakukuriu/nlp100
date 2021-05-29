package main

import (
	"strings"
)

func Ngram_words(n int, s string) [][]string {
	words := strings.Split(s, " ")
	var ngrams [][]string
	for i, j := 0, n; j <= len(words); i, j = i+1, j+1 {
		ngrams = append(ngrams, words[i:j])
	}
	return ngrams
}

func Ngram_letters(n int, s string) []string {
	letters := []rune(s)
	var ngrams []string
	for i, j := 0, n; j <= len(letters); i, j = i+1, j+1 {
		ngrams = append(ngrams, string(letters[i:j]))
	}
	return ngrams
}

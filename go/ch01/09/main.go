package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

func typoglycemia(s string) string {
	runes := []rune(s)
	subRunes := runes[1 : len(runes)-1]
	rand.Seed(time.Now().UnixNano())
	rand.Shuffle(len(subRunes), func(i, j int) { subRunes[i], subRunes[j] = subRunes[j], subRunes[i] })
	return string(runes)
}

func main() {
	s := "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
	words := strings.Split(s, " ")

	for i, w := range words {
		if len([]rune(w)) > 4 {
			words[i] = typoglycemia(w)
		}
	}

	fmt.Println(strings.Join(words, " "))

}

package main

import (
	"fmt"
	"strings"
)

func main() {
	s := "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
	rep := strings.NewReplacer(",", "", ".", "")
	var numbers []int

	for _, w := range strings.Split(s, " ") {
		numbers = append(numbers, len([]rune(rep.Replace(w))))
	}

	fmt.Println(numbers)
}

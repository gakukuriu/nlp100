package main

import (
	"fmt"
)

func main() {
	s := "パタトクカシーー"
	s2 := ""
	i := 0

	for _, c := range s {
		if i%2 == 0 {
			s2 = s2 + string(c)
		}
		i++
	}

	fmt.Println(s2)
}

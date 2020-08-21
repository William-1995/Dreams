package main

import (
	"fmt"
	"os"
)

func main() {
	var slice []int
	fmt.Println(len(slice))
	fmt.Println(cap(slice))

	var s, sep string
	for i := 1; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = " "
	}
	fmt.Println(s, os.Args)
}

package main

import "fmt"

func lengthOfLongestSubstring(s string) int {
	charmap := make(map[rune]int)

	res := 0
	i := 0

	for j, ch := range s {
		if value, exists := charmap[ch]; exists && i < value {
			i = value
		}
		if res < j-i+1 {
			res = j - i + 1
		}
		charmap[ch] = j + 1
	}

	return res
}

func main() {
	fmt.Println(lengthOfLongestSubstring("abcabc"))
}

package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {
	// 0ms; 3.8MB
	numMap := make(map[int]int)
	for i, k := range nums {
		if i2, ok := numMap[target - k]; ok {
			return []int {i2, i}
		} else {
			numMap[k] = i
		}
	}
	return []int {0, 1}
}

func main() {
	fmt.Println(twoSum([]int{2,7,11,15}, 9))
}

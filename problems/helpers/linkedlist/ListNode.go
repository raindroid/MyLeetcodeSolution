package main
import "fmt"

type ListNode struct {
    Val int
    Next *ListNode
}

func createLinkedList(li []int) *ListNode {
	root := &ListNode{li[0], nil}
	next := root
	for _, item := range li[1:] {
		next.Next = &ListNode{item, nil}
		next = next.Next
	}
	return root
}

func printLinkedList(node *ListNode) {
	if node != nil {
		fmt.Print(node.Val, " ")
		printLinkedList(node.Next)
	} else {
		fmt.Println()
	}
}
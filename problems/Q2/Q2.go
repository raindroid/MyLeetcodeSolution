/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
package main

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    result := &ListNode{}
    var digit *ListNode = nil
	carry := (l1.Val + l2.Val) / 10
	for ; (l1 != nil || l2 != nil || carry != 0); {
		if digit == nil {
			digit = result
		} else {
			digit.Next = &ListNode{}
			digit = digit.Next
		}
		l1_val, l2_val := 0, 0
		if l1 != nil { l1_val = l1.Val; l1 = l1.Next }
		if l2 != nil { l2_val = l2.Val; l2 = l2.Next }

		sum := carry + l1_val + l2_val
		digit.Val = sum % 10
		carry = sum / 10
	}
    return result
}

func main() {
	printLinkedList(addTwoNumbers(
		createLinkedList([]int {2, 4, 3}),
		createLinkedList([]int {5, 6, 4})))
}
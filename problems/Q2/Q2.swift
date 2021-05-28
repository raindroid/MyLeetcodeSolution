/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        let root = ListNode()
        var digit: ListNode? = nil
        var carry = 0
        var l1Digit = l1
        var l2Digit = l2
        while (l1Digit != nil || l2Digit != nil || carry != 0) {
            if let digitNode = digit {
                digitNode.next = ListNode()
                digit = digitNode.next
            } else {
                digit = root
            }
            var sum = carry
            if let l1Node = l1Digit {
                sum += l1Node.val
                l1Digit = l1Node.next
            }
            if let l2Node = l2Digit {
                sum += l2Node.val
                l2Digit = l2Node.next
            }
            carry = sum / 10;
            digit!.val = sum % 10
        }
        return root
    }
}

ListNode.printLinkedList(Solution().addTwoNumbers(
    ListNode.createListNode([2, 4, 3]),
    ListNode.createListNode([5, 6, 4])
))
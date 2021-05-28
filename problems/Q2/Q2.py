# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.path.append('../helpers/linkedlist')
from ListNode import *


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        digit = None
        carry = 0
        while l1 or l2 or carry:
            if not digit: digit = res
            else:
                digit.next = ListNode()
                digit = digit.next
            value = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            carry = value // 10
            digit.val = value % 10
        return res

printLinkedList(Solution()
                    .addTwoNumbers(
                        createLinkedList([2,4,3]), 
                        createLinkedList([5,6,4])
                    )
                )
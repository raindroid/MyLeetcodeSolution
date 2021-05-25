/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
const {createLinkedList, ListNode, printLinkedList} = require('../helpers/linkedlist/ListNode.js');

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let res = new ListNode()
    let digit = null
    let carry = 0
    while (l1 || l2 || carry) {
        if (!digit) digit = res
        else {
            digit.next = new ListNode()
            digit = digit.next
        }
        let value = carry + (l1?l1.val:0) + (l2?l2.val:0)
        l1 = l1?l1.next:0
        l2 = l2?l2.next:0
        carry = Math.floor(value / 10)
        digit.val = value % 10
    }
    return res
};

printLinkedList(addTwoNumbers(
                    createLinkedList([2, 4, 3]),
                    createLinkedList([5, 6, 4])
                ))
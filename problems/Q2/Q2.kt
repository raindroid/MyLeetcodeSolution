/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun addTwoNumbers(il1: ListNode?, il2: ListNode?): ListNode? {
        var res = ListNode(0)
        var digit: ListNode? = null
        var carry: Int = 0
        var l1 = il1
        var l2 = il2
        while (l1 != null || l2 != null || carry != 0) {
            if (digit == null) digit = res
            else {
                digit.next = ListNode()
                digit = digit.next
            }
            val value: Int = carry + (l1?.`val`?:0) + (l2?.`val`?:0)
            l1 = l1?.let{it.next}
            l2 = l2?.let{it.next}
            carry = value / 10
            digit?.apply {`val` = value % 10}
        }
        return res
    }
}

fun main() {
    println("Test");
}
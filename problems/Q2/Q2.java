package problems.Q2;
import java.util.Arrays;
import problems.helpers.linkedlist.ListNode;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        var res = new ListNode();
        ListNode digit = null;
        int carry = 0;
        while (l1 != null || l2 != null || carry != 0) {
            if (digit == null) digit = res;
            else {
                digit.next = new ListNode();
                digit = digit.next;
            }
            int value = carry + (l1 != null ?l1.val:0) + (l2 != null ?l2.val:0);
            l1 = l1 != null ?l1.next:l1;
            l2 = l2 != null ?l2.next:l2;
            carry = value / 10;
            digit.val = value % 10;
        }
        return res;
    }
}

class Q2 {
    public static void main(String[] args) {
        ListNode.printLinkedList(
            new Solution().addTwoNumbers(
                ListNode.createLinkedList(Arrays.asList(2, 4, 3)), 
                ListNode.createLinkedList(Arrays.asList(5, 6, 4))
            )
        );
    }
}

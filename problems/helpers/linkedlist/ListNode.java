import java.util.List;

public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    
    static public ListNode createLinkedList(List<Integer> li) {
        ListNode root = new ListNode(li.get(0));
        ListNode next = root;
        for (int item : li.subList(1, li.size())) {
            next.next = new ListNode(item);
            next = next.next;
        }
        return root;
    }

    static public void printLinkedList(ListNode node) {
        while(node != null) {
            System.out.print(node.val + " ");
            node = node.next;
        }
        System.out.println("");
    }
}
public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init() { self.val = 0; self.next = nil; }
    public init(_ val: Int) { self.val = val; self.next = nil; }
    public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }

    static public func createListNode(_ li: [Int]) -> ListNode {
        let root = ListNode(li[0])
        var next = root
        for item in li[1...] {
            next.next = ListNode(item)
            next = next.next ?? ListNode()
        }
        return root
    }

    static public func printLinkedList(_ node: ListNode?) {
        if let listNode = node {
            print(listNode.val, terminator:" ")
            printLinkedList(listNode.next)
        } else {
            print("\n")
        }
    }
}
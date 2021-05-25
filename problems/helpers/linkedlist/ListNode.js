function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

module.exports.ListNode = ListNode

module.exports.createLinkedList = (li) => {
    root = new ListNode(li[0])
    next = root
    for (i = 1; i < li.length; i++) {
        next.next = new ListNode(li[i])
        next = next.next
    }
    return root
}

module.exports.printLinkedList = (node) => {
    output = ""
    while(node != null) {
        output += node.val + " "
        node = node.next
    }
    console.log(output)
}
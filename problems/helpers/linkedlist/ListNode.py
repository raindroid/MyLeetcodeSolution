class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedList(li):
    assert len(li) > 0, "List is empty"
    root = ListNode(li[0])
    next = root
    for item in li[1:]:
        next.next = ListNode(item)
        next = next.next

    return root

def printLinkedList(node):
    if node != None:
        print(node.val, end=' ')
        printLinkedList(node.next)
    else:
        print()

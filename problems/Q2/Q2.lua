package.path = '../helpers/linkedlist/ListNode.lua;'..package.path
require 'ListNode'

local function addTwoNumbers(l1, l2)
    local res = ListNode({})
    local digit = nil
    local carry = 0
    while l1 or l2 or carry ~= 0 do
        if not digit then
            digit = res
        else
            digit.next_node = ListNode({})
            digit = digit.next_node
        end
        value = carry + (l1 and l1.val or 0) + (l2 and l2.val or 0)
        l1 = l1 and l1.next_node
        l2 = l2 and l2.next_node
        carry = math.floor( value / 10 )
        digit.val = value % 10
    end
    return res
end

printLinkedList(
    addTwoNumbers(
        createLinkedList({2,4,3}),
        createLinkedList({5,6,4})
    )
)
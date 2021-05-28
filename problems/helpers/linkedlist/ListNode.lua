ListNode = setmetatable({}, {
    __call = function(my, newNode)
        newNode.__index = {val = 0, next_node = nil}
        return setmetatable({val = newNode.val, next_node = newNode.next_node}, self)
    end
})
ListNode.__index = ListNode

function createLinkedList(li)
    local root = ListNode({val=li[1]})  -- array starts at index 1
    local node = root
    for i, item in ipairs(li) do
        if i > 1 then
            node.next_node = ListNode({val=item})
            node = node.next_node
        end
    end
    return root
end

function printLinkedList(node)
    if node ~= nil then
        io.write(node.val, " ")
        printLinkedList(node.next_node)
    else
        print()
    end
end
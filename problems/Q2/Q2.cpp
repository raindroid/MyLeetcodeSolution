/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include "../helpers/linkedlist/ListNode.hpp"

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        auto res = new ListNode();
        ListNode* digit = nullptr;
        int carry = 0;
        while (l1 || l2 || carry) {
            if (! digit) digit = res;
            else {
                digit->next = new ListNode();
                digit = digit->next;
            }
            int value = carry + (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
            carry = value / 10;
            digit->val = value % 10;
        }
        return res;
    }
};

int main() {
    printLinkedList((new Solution())
                        ->addTwoNumbers(
                            createLinkedList({2,4,3}),
                            createLinkedList({5,6,4})
                        )
                   );
}
#include <vector>
#include <iostream>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

inline ListNode* createLinkedList(std::vector<int> li) {
    ListNode* root = new ListNode(li[0]);
    ListNode* next = root;
    for (int i = 1; i < li.size(); i++) {
        next->next = new ListNode(li[i]);
        next = next->next;
    }
    return root;
}

inline void printLinkedList(ListNode* node) {
    while(node != NULL) {
        std::cout << node->val << " ";
        node = node->next;
    }
    std::cout << std::endl;
}
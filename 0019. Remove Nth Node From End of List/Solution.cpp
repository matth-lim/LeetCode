// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* l = head;
        ListNode* r = head;
        for (int i = 0; i < n; i++)
            l = l->next;
        if (!l) return head->next;
        while (l->next)
        {
            l = l->next;
            r = r->next;
        }
        r->next = r->next->next;
        return head;
    }
};
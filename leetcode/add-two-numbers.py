/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    // two phases
    // one when both linked lists have nodes, add the ith nodes of both
    // store ones in new linked list
    // store tens in a carry over variable that you add
    int tens = 0;

    // really just an array of linked nodes, since all in a row in memory
    struct ListNode* result = malloc(sizeof(struct ListNode) * 101);
    struct ListNode* head = result;

    while (l1 != NULL || l2 != NULL) {
        int v1 = 0;
        int v2 = 0;
        if (l1) { 
            v1 = l1->val; 
            l1 = l1->next;
        }
        if (l2) { 
            v2 = l2->val; 
            l2 = l2->next;
        }

        result->val = (v1 + v2 + tens) % 10;
        tens = (v1 + v2 + tens) / 10;

        // on last iteration, this ensures last node, doesn't link to a garbage node at end
        if (l1 != NULL || l2 != NULL || tens != 0) {
            result->next = result + 1;
            result = result->next;
        }
    }

    // final carry forward, if tens do not equal 0
    if (tens != 0) {
        result->val = tens;
    }
    result->next = NULL;
    return head;
}
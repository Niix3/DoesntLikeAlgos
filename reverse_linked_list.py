# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head:ListNode) -> ListNode:
    prev_one = None
    while head is not None:
        next_one = head.next
        head.next = prev_one
        prev_one = head

        head = next_one

    return prev_one



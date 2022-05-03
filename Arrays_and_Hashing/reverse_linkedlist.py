class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        print(curr)
        prev = None
        while curr.next is not None:
            next = curr.next
            curr.next = prev
            curr = next
        head = curr
        return head

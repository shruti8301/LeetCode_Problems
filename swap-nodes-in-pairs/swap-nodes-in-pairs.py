# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        head_next=head.next.next
        first=head
        second=head.next
        second.next=first
        first.next=self.swapPairs(head_next)
        return second
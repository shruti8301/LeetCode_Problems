# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            prevN= ListNode(0)
            prevN.next=head
            temp=head
            prev=prevN
            while temp:
                if temp.val==val:
                    prev.next=temp.next
                else:
                    prev=prev.next
                temp=temp.next
            return prevN.next
        
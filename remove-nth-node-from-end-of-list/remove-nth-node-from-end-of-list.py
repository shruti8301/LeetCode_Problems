# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return 
        l=0
        temp=head
        while temp:
            l+=1
            temp=temp.next
        
        a=l-n
        
        if a==0:
            head=head.next
        else:
            temp=head
            for _ in range(a-1):
                temp=temp.next
            temp.next=temp.next.next
        return head
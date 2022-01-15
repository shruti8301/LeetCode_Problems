# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        temp = head
        c=0
        while (temp.next is not None):
            temp=temp.next
            c+=1
        c+=1
        k=k%c
        if k==0:
            return head
        temp.next=head
        temp=head
        
        for i in range(c-k-1):
            temp=temp.next

        curr=temp.next
        temp.next=None
        return curr
    
            
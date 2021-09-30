# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        if head is None:
            return 
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        new_lst = arr[::-1]
        if(arr==new_lst):
            return True
       
        
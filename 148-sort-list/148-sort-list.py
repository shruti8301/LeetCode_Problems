# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        arr=arr[::-1]
        d=ListNode();
        point=d
        while len(arr)>0:
            val=arr.pop()
            point.next=ListNode(val)
            point=point.next
        return d.next
        print(arr)
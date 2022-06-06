# Definition for singly-linked list.
#class ListNode:
   # def __init__(self, x):
       # self.val = x
       # self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d={}
        while headA:
            d[headA]=1
            headA=headA.next
        while headB:
            if d.get(headB):
                return headB
            headB=headB.next
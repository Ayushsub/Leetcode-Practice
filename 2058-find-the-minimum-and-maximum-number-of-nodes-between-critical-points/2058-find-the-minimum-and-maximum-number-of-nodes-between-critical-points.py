# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        curr=head.next
        pos=1
        first=-1
        last=-1
        mind=float('inf')
        while curr.next:
            if (curr.val>prev.val and curr.val>curr.next.val) or (curr.val<prev.val and curr.val<curr.next.val):
                if first==-1:
                    first=pos
                if last!=-1:
                    mind=min(mind,pos-last)
                last=pos
            prev=curr
            curr=curr.next
            pos+=1
        if first==last:
            return [-1,-1]
        return [mind,last-first]
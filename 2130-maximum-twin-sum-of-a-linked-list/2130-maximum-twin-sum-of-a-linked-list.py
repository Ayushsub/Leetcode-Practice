# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        i,j=0,len(a)-1
        ans=0
        while i<j:
            ans=max(ans,a[i]+a[j])
            i+=1
            j-=1
        return ans


# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         slow=head
#         fast=head
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#         prev=None
#         while slow:
#             nxt=slow.next
#             slow.next=prev
#             prev=slow
#             slow=nxt
#         ans=0
#         first=head
#         second=prev
#         while second:
#             ans=max(ans,first.val+second.val)
#             first=first.next
#             second=second.next
#         return ans
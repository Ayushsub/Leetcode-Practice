# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque([root])
        level=1
        ans=1
        m=float("-inf")
        while q:
            n=len(q)
            s=0
            for i in range(n):
                node=q.popleft()
                val=node.val
                s+=val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s>m:
                m=s
                ans=level
            level+=1
        return ans
        
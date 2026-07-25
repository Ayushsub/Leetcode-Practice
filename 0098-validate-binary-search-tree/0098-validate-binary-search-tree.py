# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l,r=float('-inf'),float('inf')
        def check(low,high,node):
            if not node:
                return True
            if not (low<node.val<high):
                return False
            return check(low,node.val,node.left) and check(node.val,high,node.right)
        return check(l,r,root)

        
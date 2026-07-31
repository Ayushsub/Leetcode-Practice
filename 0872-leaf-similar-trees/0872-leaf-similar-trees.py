# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf(node):
            a=[]
            def inorder(node):
                if not node:
                    return
                inorder(node.left)
                if not node.left and not node.right:
                    a.append(node.val)
                inorder(node.right)
            inorder(node)
            return a
        return leaf(root1)==leaf(root2)
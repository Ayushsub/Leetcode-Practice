# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp={v:i for i,v in enumerate(inorder)}
        def dfs(l,r,pre):
            if l>r:
                return None,pre
            root=TreeNode(preorder[pre])
            mid=mp[root.val]
            pre+=1
            root.left,pre=dfs(l,mid-1,pre)
            root.right,pre=dfs(mid+1,r,pre)
            return root,pre
        root,_=dfs(0,len(inorder)-1,0)
        return root
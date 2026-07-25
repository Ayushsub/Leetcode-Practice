# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos={v:i for i,v in enumerate(postorder)}
        def dfs(preL,preR,postL,postR):
            if preL>preR:
                return None
            root=TreeNode(preorder[preL])
            if preL==preR:
                return root
            leftRoot=preorder[preL+1]
            idx=pos[leftRoot]
            leftSize=idx-postL+1
            root.left=dfs(preL+1,
                          preL+leftSize,
                          postL,
                          idx)
            root.right=dfs(preL+leftSize+1,
                           preR,
                           idx+1,
                           postR-1)
            return root
        return dfs(0,len(preorder)-1,0,len(postorder)-1)
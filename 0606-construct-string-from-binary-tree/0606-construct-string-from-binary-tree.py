# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = []
        self.dfs(root, result)
        return ''.join(result)
    
    def dfs(self, root, result):
        if not root:
            return
        
        result.append(str(root.val))
        
        if not root.left and not root.right:
            return
        
        result.append('(')
        self.dfs(root.left, result)
        result.append(')')
        
        if root.right:
            result.append('(')
            self.dfs(root.right, result)
            result.append(')')

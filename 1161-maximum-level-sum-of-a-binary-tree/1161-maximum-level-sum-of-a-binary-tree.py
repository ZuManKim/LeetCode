# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum, ans, level = -1e5, 0, 0
        q = deque()
        q.append(root)
        
        while q:
            level += 1
            sumAtCurrentLevel = 0
            
            for _ in range(len(q)):
                node = q.popleft()
                sumAtCurrentLevel += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if sumAtCurrentLevel > maxSum:
                maxSum, ans = sumAtCurrentLevel, level
        
        return ans
# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1416543804/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0
        return self.dfs(root, height)
        
    def dfs(self, node, height):
        if node is None:
            return 0

        l = self.dfs(node.left, height+1)
        r = self.dfs(node.right, height+1)
        return max(height+1, l, r)

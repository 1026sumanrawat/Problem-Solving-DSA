# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swapChild(root)
        return root
    def swapChild(self,node):
        if node is None:
            return
        l = node.left
        r = node.right
        node.left = r
        node.right = l
        self.swapChild(node.left)
        self.swapChild(node.right)

        
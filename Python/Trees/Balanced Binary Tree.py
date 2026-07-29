# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        return 1 + max(left,right)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        leftBalanced = self.isBalanced(root.left)
        rightBalanced = self.isBalanced(root.right)
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        if abs(leftDepth - rightDepth) <= 1 and leftBalanced and rightBalanced:
            return True
        else:
            return False


# O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            
            left = helper(root.left)
            if left == -1:
                return -1
            right = helper(root.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)
        return helper(root) != -1

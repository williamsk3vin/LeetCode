# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(node1, node2):
            if node1 is None and node2 is None:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            if node1.val == node2.val:
                return (
                    helper(node1.left, node2.left) and
                    helper(node1.right, node2.right)
                )
        if root is None:
            return False

        if helper(root, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot)
            or
            self.isSubtree(root.right, subRoot)
        )

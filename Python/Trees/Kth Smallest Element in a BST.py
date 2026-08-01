# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def helper(root, k):
            if root is None:
                return None
            left = helper(root.left,k)
            if left is not None:
                return left

            self.count += 1
            if k == self.count:
                return root.val

            return helper(root.right,k)

        return helper(root,k)

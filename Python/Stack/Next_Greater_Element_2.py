class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        greater = [-1] * len(nums)
        stack = []

        for i in range(len(nums) * 2):
            index = i % len(nums)
            while stack and nums[index] > nums[stack[-1]]:
                popped = stack.pop()
                greater[popped] = nums[index]

            if i < len(nums):
                stack.append(index)
        return greater



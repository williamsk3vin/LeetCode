class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greaterElement = [-1] * len(nums1)
        maps = {}

        for nums in nums2:
            while stack and nums > stack[-1]:
                value = stack.pop()
                maps[value] = nums
            stack.append(nums)
        
        for idx , nums in enumerate(nums1):
            if nums in maps:
                greaterElement[idx] = maps[nums]

        return greaterElement       

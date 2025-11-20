class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSum = nums[0]
        for i in range(1,len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSub = max(maxSub, currentSum)
        return maxSub

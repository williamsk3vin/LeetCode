class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        for left in range(1,len(nums)-k+1):
            window_sum = window_sum - nums[left - 1] + nums[left + k - 1]
            max_sum = max(max_sum, window_sum) 
        return max_sum / k

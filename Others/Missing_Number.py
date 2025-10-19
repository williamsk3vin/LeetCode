class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        a = len(nums)
        a_sum = (a * (a + 1)) // 2
        missing = a_sum - s
        return missing

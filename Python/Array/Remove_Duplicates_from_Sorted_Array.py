class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        read = 0
        for write in range(1, len(nums)):
            if nums[write] != nums[read]:
                read += 1
                nums[read] = nums[write]
        return read + 1

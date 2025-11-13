class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        counter = 0
        while left <= right:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
            elif nums[right] == val:
                right -= 1
            else:
                left += 1
                counter += 1
        return counter
            

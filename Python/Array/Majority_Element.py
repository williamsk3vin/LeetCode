class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = {}
        for num in nums:
            majority[num] = majority.get(num,0) + 1
        return max(majority, key=majority.get)


#Boyer-Moore
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif candidate == num:
                count += 1
            elif candidate != num:
                count -= 1
        return candidate

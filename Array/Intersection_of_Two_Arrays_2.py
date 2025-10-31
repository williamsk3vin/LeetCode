class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = []
        checker = {}
        for num in nums2:
            checker[num] = checker.get(num,0) + 1
        for num in nums1:
            if num in checker and checker[num] > 0:
                intersect.append(num)
                checker[num] -= 1
        return intersect

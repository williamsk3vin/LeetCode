# Time n-squared
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        for num in nums1:
            if num in nums2 and num not in seen:
                seen.add(num)
        return list(seen)


# Time O(n + m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        answer = set()
        for num in nums2:
            if num in set1:
                answer.add(num)
        return list(answer)

# Time O(log n) + O(log m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        left = 0
        right = 0
        answer = set()
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums2[right] < nums1[left]:
                right += 1
            elif nums1[left] == nums2[right]:
                answer.add(nums1[left])
                left += 1
                right += 1
        return list(answer)

# Time O(n log n) + O(m log m)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        answer = set()
        for num in nums2:
            left = 0
            right = len(nums1) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums1[mid] == num:
                    answer.add(num)
                    left += 1
                    right -= 1
                elif num > nums1[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return list(answer)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        containerMax = 0
        left = 0
        right = len(height) - 1
        while left < right:
            width = right - left
            container = min(height[left],height[right]) * width
            containerMax = max(container, containerMax)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return containerMax

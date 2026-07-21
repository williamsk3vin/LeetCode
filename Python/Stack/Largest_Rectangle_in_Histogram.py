class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        nsl = [-1] * len(heights)
        nsr = [len(heights)] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nsl[i] = stack[-1]
            stack.append(i)

        stack.clear()

        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nsr[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(len(heights)):
            width = nsr[i] - nsl[i] - 1
            maxArea = max(maxArea,heights[i] * width)

        return maxArea

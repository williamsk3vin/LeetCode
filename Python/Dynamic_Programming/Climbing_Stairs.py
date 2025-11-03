class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            b, a = b + a, b
        return b

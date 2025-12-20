class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        r = 0
        while n >= 0:
            r += 1
            n -= r
            if n >= 0:
                rows += 1
        return rows



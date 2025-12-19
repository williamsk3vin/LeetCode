class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        
        low = 0
        high = int(log(n, 4)) + 1
        
        while low <= high:
            mid = (low + high) // 2
            power = 4 ** mid
            if power == n:
                return True
            elif power > n:
                high = mid - 1
            else:
                low = mid + 1
        return False
            

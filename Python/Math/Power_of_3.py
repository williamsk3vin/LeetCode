class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        low = 0
        high = int(log(n, 3)) + 1
        
        
        while low <= high:
            mid = (low + high) // 2
            power = 3 ** mid
            if power == n:
                return True
            elif power < n:
                low = mid + 1
            elif power > n:
                high = mid - 1
        return False


# No loops
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0 and (3**19) % n == 0:
            return True
        return False

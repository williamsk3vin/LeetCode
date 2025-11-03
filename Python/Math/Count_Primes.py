class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        is_Prime = [True] * n
        is_Prime[0] = is_Prime[1] = False
        p = 2
        
        while p * p < n:
            if is_Prime[p]:   
                for i in range(p * p,n,p):
                    is_Prime[i] = False
            p += 1
        return sum(is_Prime)

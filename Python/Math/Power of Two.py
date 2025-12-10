##First Solution
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #binary problem
        #whole integer power of 2
        # 0, 2, 4, 16, 32, 64 ...
        if n <= 0:
            return False
        x = math.log(n, 2)
        return n == (2 ** (floor(x)))

  #Bitwise 
  class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False     
        elif n & (n - 1) == 0:
            return True
        else:
            return False

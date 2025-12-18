class Solution:
    def isHappy(self, n: int) -> bool:
        sq_sum = 0
        seen = []

        while n:
            r = n % 10
            sq_sum += r ** 2
            n //= 10
            if n == 0 and sq_sum not in seen:
                seen.append(sq_sum)
                n = sq_sum
                sq_sum = 0
            elif n == 0 and sq_sum == 1:
                return True
            elif n == 0 and sq_sum in seen:
                return False

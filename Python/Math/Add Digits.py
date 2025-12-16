#Without Loops
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9


#With Loops
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        
        total = 0
        while num:
            total += num % 10
            if num // 10 == 0 and total >= 10:
                num = total
                total = 0
            else:
                num //= 10
        return total

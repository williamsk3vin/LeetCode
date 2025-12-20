class Solution:
    def convertToBase7(self, num: int) -> str:
        baseSeven = 0
        counter = 1
        sign = 1 if num >= 0 else -1
        num = abs(num)
        while num:
            baseSeven += (num % 7) * counter
            num //= 7
            counter *= 10
        return str(sign * baseSeven)

#No str conversion
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = x
        rev = 0
        while y:
            pop = y % 10
            rev = rev * 10 + pop
            y //= 10
        if rev == x:
            return True
        return False

#Str conversion
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        if x == x[::-1]:
            return True
        return False

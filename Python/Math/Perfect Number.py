class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        search = int(num ** 0.5)
        factorSum = 1
        for i in range(2, search + 1):
            factor = num / i
            if factor == int(factor):
                factorSum += i
                factorSum += factor
        if factorSum == num:
            return True
        return False

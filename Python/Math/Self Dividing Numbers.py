class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def self_dividing(self, num: int) -> bool:
            x = num
            while x:
                digit = x % 10
                if digit == 0 or num % digit != 0:
                    return False
                x //= 10
            return True
        ans = []
        for i in range(left, right + 1):
            if self_dividing(self,i):
                ans.append(i)
        return ans

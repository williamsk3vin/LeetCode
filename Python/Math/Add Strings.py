#First Attempt
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1) - 1, len(num2) - 1
        carry, a, b = 0, 0, 0
        result = ''
        while l1 >= 0 or l2 >= 0:
            if l1 < 0:
                a = ord('0') - ord('0')
                b = ord(num2[l2]) - ord('0')
            elif l2 < 0:
                a = ord(num1[l1]) - ord('0')
                b = ord('0') - ord('0')
            else:
                a = ord(num1[l1]) - ord('0')
                b = ord(num2[l2]) - ord('0')
            c = a + b + carry
            carry = 0
            if c > 9:
                carry = c // 10
                c = c % 10
            result = str(c) + result
            l1 -= 1
            l2 -= 1
        if carry:
            result = str(carry) + result
        return result

#Cleaner Version
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1) - 1, len(num2) - 1
        carry, a, b = 0, 0, 0
        result = ''
        while l1 >= 0 or l2 >= 0:
            a = 0 if l1 < 0 else ord(num1[l1]) - ord('0')
            b = 0 if l2 < 0 else ord(num2[l2]) - ord('0')

            result = str((a + b + carry) % 10) + result
            carry = (a + b + carry) // 10
            
            l1 -= 1
            l2 -= 1
        if carry:
            result = str(carry) + result
        return result

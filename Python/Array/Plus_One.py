class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        if digits[-1] == 10:
            digits[-1] = 0
            carry = 1
            for i in range(-2, -len(digits) - 1, -1):
                digits[i] += carry
                if digits[i] < 10:
                    return digits
                digits[i] = 0
        if carry:
            digits.insert(0, carry)        
        return digits
                

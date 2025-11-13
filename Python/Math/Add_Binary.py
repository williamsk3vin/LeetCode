class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''
        i = len(a) - 1
        j = len(b) - 1

        while (i >= 0) or (j >= 0) or (carry == 1):
            if i >= 0:
                bitA = int(a[i])
                i -= 1
            else:
                bitA = 0
            if j >= 0:
                bitB = int(b[j])
                j -= 1
            else:
                bitB = 0
            
            total = bitA + bitB + carry
            result = str(total % 2) + result
            carry = total // 2
        return result

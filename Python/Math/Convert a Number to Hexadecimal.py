class Solution:
    def toHex(self, num: int) -> str:
        dec2hex = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        hexString = ''

        x = num if num >= 0 else (2**32 - abs(num))

        if num == 0:
            return '0'

        while x:
            r = x % 16
            if r > 9:
                hexString = dec2hex[r] + hexString
            else:
                hexString = str(r) + hexString
            x //= 16

        return hexString

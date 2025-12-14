class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        length = len(columnTitle) - 1
        num = 0
        base = 26
        for letter in columnTitle:
            num += (ord(letter) - 64) * (base ** length)
            length -= 1
        return num

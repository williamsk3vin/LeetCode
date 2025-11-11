class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        bounce = 0
        zags = [''] * numRows
        direction = 1
        for i in range(len(s)):

            zags[bounce] += s[i]

            bounce += direction
            if bounce >= numRows - 1:
                direction = -1  # start going down
            elif bounce <= 0:
                direction = 1
        word = "".join(zags)
        return word

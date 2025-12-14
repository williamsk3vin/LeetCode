class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ''

        while columnNumber:
            remainder = columnNumber % 26
            if remainder == 0:
                char = 'Z'
            else:
                char = chr(remainder + ord('A') - 1)
            title = char + title

            columnNumber //= 26
            if remainder == 0:
                columnNumber -= 1
        return title

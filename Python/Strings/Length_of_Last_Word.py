#One liner
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


#Iterating through string
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = []
        count = 0
        for i in s:
            if i != " ":
                count += 1
            elif count > 0 and i == ' ':
                l.append(count)
                count = 0
        if count > 0:
            l.append(count)
        return l[-1]

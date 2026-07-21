class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join([char.lower() for char in s if char.isalnum()])

        return cleaned == cleaned[::-1]


#Two Pointer
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(filter(str.isalnum, s)).lower()
        left = 0
        right = len(s2) - 1
        while left <= right:
            if s2[left] == s2[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

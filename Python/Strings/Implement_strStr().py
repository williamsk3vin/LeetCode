class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        #len(haystack) - len(needle) ensures we can check i in haystack for every needle
        for i in range(len(haystack) - len(needle) + 1):
            # stops at i + len(needle) - 1
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

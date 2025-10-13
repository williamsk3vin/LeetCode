class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        increment = 1
        counter = 0
        min_word = min(strs, key=len)
        
        if len(min_word) == 0:
            return ""
        
        while counter < len(min_word):
            for word in strs:
                if word[counter] != min_word[counter]:
                    return prefix
            prefix += min_word[counter]
            counter += 1
        return prefix

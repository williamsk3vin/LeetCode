class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_len = 0
        start = 0
        last_seen = {}

        for i in range(len(s)):
            char = s[i]
            #If char is in current sliding window
            #change start to the last time char has been seen + 1
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            #update dictionary value for char 
            last_seen[char] = i
            # (i - start + 1) because i is current index
            # we start at 'start' (i - start) is substring length
            # add 1 because at start = 0, len is 1
            substring_len = max(substring_len, i - start + 1)
        return substring_len
            

#Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

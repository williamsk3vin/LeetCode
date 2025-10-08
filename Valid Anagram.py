class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        for letter in s:
            counter[letter] = counter.get(letter, 0) + 1
        
        for letter in t:
            if letter in counter:
                counter[letter] -= 1
            elif letter not in counter:
                return False
        return all(value == 0 for value in counter.values())

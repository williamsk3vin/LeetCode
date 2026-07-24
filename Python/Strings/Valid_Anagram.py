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


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        if len(s) != len(t):
            return False
        for i in s:
            counter[i] = counter.get(i, 0) + 1
        
        for j in t:
            if j in counter:
                counter[j] -= 1
                if counter[j] < 0:
                    return False
            else:
                return False
        for value in counter.values():
            if value != 0:
                return False
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if count.get(ch, 0) == 0:
                return False
            count[ch] -= 1

        return True

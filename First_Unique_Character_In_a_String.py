class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        unique = []

        for letter in s:
            # Update count
            counter[letter] = counter.get(letter, 0) + 1

            # If first occurrence, add to unique list
            if counter[letter] == 1:
                unique.append(letter)

            # Clean up front of the list
            while unique and counter[unique[0]] > 1:
                unique.pop(0)  # remove from front

        # Return index of first unique char, or -1 if none
        if unique:
            return s.index(unique[0])
        else:
            return -1

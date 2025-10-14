class Solution:
    def romanToInt(self, s: str) -> int:
        r_to_i_dict = {'I': 1, 'V' : 5, 'X': 10,
                       'L':50, 'C':100, 'D':500, 'M':1000 }
        total = 0
        
        for i in range(len(s) - 1):
            if r_to_i_dict[s[i]] < r_to_i_dict[s[i + 1]]:
                total -= r_to_i_dict[s[i]]
            else:
                total += r_to_i_dict[s[i]]
        total += r_to_i_dict[s[-1]]
        
        return total

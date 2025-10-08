class Solution:
    def myAtoi(self, s: str) -> int:
        MAX = 2**31 - 1
        MIN = -2**31
        num = 0
        
        #strip leading spaces
        s = s.lstrip()
        if not s:
            return 0
        
        #handling sign
        sign = 1
        start_index = 0
        if s[0] == "-":
            sign = -1
            start_index = 1
        elif s[0] == '+':
            start_index = 1

        #Build num
        for letter in s[start_index:]:
            if letter.isdigit():
                num = num * 10 + int(letter)
            else:
                break
        
        #apply sign
        num *= sign 
        
        #check boundaries
        if num > MAX:
            return MAX
        elif num < MIN:
            return MIN
        
        return num
                
            

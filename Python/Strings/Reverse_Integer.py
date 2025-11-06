class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31
        MIN = -2**31 #Doesn't need to be here
        
        sign = 1 if x >= 0 else -1
        rev = 0
        x = abs(x)
        
        while x != 0:
            pop = x % 10    #extracts last digit
            x //= 10    #removes last digit
            
            if rev > (MAX - pop) // 10: #checks if rev is Greater than the Max number minus the last digit with the last digit removed
                return 0                #if rev is greater than that condition, it will be exceed the max in the next step
            
            rev = rev * 10 + pop
            
        return sign * rev

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            #if open bracket, append to stack
            if ch in mapping.values():
                stack.append(ch)
                #if closing bracket
            elif ch in mapping:
                #if closing bracket is not in stack or at end of stack
                if not stack or stack[-1] != mapping[ch]:
                    return False
                #if conditions arent met, remove last item in stack
                stack.pop()
            else:
                return False
        
        return not stack

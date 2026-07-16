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



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False

        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False

                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True

class Solution:
    def buildStack(self, s: str) -> str:
        stack = []
        for char in s:
            if char ==  '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.buildStack(s) == self.buildStack(t)
        

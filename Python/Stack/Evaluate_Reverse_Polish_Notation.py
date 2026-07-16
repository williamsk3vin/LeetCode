class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
            }
        for tok in tokens:
            if tok in ops:
                right = stack.pop()
                left = stack.pop()
                stack.append(ops[tok](left,right))
            else:
                stack.append(int(tok))
        return stack[-1]

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            previous = self.stack.pop()
            span += previous[1]
        self.stack.append((price,span))
        return span

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        solution = []
        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                solution.append('FizzBuzz')
            elif i % 5 == 0:
                solution.append('Buzz')
            elif i % 3 == 0:
                solution.append('Fizz')
            else:
                solution.append(str(i))
        return solution

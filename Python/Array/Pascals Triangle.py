class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return triangle
        counter = len(triangle)
        while counter < numRows:
            triangle_step = [0] * (counter + 1)
            triangle_step[0], triangle_step[-1] = 1, 1

            prev = len(triangle[counter - 1])
            for i in range(prev - 1):
                triangle_step[i + 1] = triangle[counter - 1][i] + triangle[counter - 1][i + 1]
            triangle.append(triangle_step)
            counter += 1
        return triangle

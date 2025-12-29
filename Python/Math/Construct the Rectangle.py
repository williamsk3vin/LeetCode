class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = int(area ** 0.5)

        while width:
            if width ** 2 == area:
                return [width, width]
            L = area // width
            if L % 1 == 0 and L * width == area:
                return [L, width]
            else:
                width -= 1


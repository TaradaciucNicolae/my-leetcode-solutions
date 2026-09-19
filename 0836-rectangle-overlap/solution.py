class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        r1x1,r1y1,r1x2,r1y2 = rec1
        r2x1,r2y1,r2x2,r2y2 = rec2

        return r1x1 < r2x2 and r2x1 < r1x2 and r1y1 < r2y2 and r2y1 < r1y2

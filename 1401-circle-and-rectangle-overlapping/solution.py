class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        

        closestX_on_rectangle = max(x1, min(xCenter, x2))
        closestY_on_rectangle = max(y1, min(yCenter, y2))

        #distance from the closest point to the Center ->  (x1-x2)**2 + (y1-y2)**2

        dist = (closestX_on_rectangle - xCenter)**2 + ( closestY_on_rectangle - yCenter)**2


        if radius**2 >= dist:
            return True
        else:
            return False

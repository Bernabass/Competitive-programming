class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        min_arrows = 0
        while points:  
            arrow = points[0][1]
            min_arrows += 1

            while points and points[0][0] <= arrow: 
                points.pop(0)

        return min_arrows
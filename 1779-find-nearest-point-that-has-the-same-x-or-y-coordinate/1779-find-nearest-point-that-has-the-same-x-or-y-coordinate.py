class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = [float('inf'),-1]
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                dist = abs(x - points[i][0]) + abs(y - points[i][1])
                if dist < res[0]:
                    res = [dist,i]
        return res[1]
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        output = 0
        currPoint = points.pop()
        paths = {tuple(p): float('inf') for p in points}
        while paths:
            currMin = float('inf')
            for pt, val in paths.items():
                dist = abs(pt[0] - currPoint[0]) + abs(pt[1] - currPoint[1])
                if dist < val:
                    paths[pt] = dist
                    val = paths[pt]
                if val < currMin:
                    currMin = val
                    nextPt = pt
            output += paths.pop(nextPt)
            currPoint = nextPt
        return output
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points = list(map(tuple,points))
        n = len(points)
        slopes = defaultdict(lambda:1)
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            check = slopes.copy()
            for j in range(i+1,n):
                x2, y2 = points[j][0], points[j][1]
                if x2 - x1 == 0 and y2 - y1 == 0:
                    if "v"+str(y1) not in check:
                        slopes["v"+str(y1)] += 1
                    if "h"+str(x1) not in check:   
                        slopes["h"+str(x1)] += 1
                elif x2 - x1 == 0 and "v"+str(y1) not in check:
                    slopes["v"+str(y1)] += 1
                elif y2 - y1 == 0 and "h"+str(x1) not in check:
                    slopes["h"+str(x1)] += 1
                if 0 not in {x2-x1,y2-y1}:
                    curr_slope = (y2 - y1)/(x2 - x1)
                    intercept = y1 - curr_slope* x1
                    if (curr_slope,intercept) not in check:
                        slopes[(curr_slope,intercept)] += 1  
        if not slopes.values():
            return 1
        return max(slopes.values())
        
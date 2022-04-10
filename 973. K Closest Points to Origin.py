class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        idx=[]
        NearPoints=[]
        for i in range(len(points)):
            d=0
            for j in range(2):
                d+=(points[i][j])**(2)
            idx.append(d)
        idx.sort()
        maxx = idx[k-1]
        for i in range(len(points)):
            d=0
            for j in range(2):
                d+=(points[i][j])**(2)
            if d <= maxx:
                NearPoints.append(points[i])
        return NearPoints    
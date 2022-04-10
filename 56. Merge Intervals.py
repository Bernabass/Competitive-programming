class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        u=[]
        u.append(intervals[0])
        for i in range(1,len(intervals)):
            temp=intervals[i]
            if temp[0]<=u[-1][1]:
                u[-1][1]=max(u[-1][1],temp[1])
            else:
                u.append(temp)
        return u
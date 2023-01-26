class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def merge_intervals(intervals):
            intervals.sort()
            res = []
            res.append(intervals[0])
            for i in range(1,len(intervals)):
                current = intervals[i]
                if current[0] < res[-1][1]:
                    res[-1][1] = max(res[-1][1],current[1])
                else:
                    res.append(current)
            return res
        
        uniques = set(s)
        intervals = []
        
        for i in uniques:
            intervals.append([s.index(i),s.rfind(i)])
            
        res = merge_intervals(intervals)
        
        for idx, merged in enumerate(res):
            res[idx] = merged[1] - merged[0] + 1
            
        return res
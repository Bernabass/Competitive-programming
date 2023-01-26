class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def merge_intervals(intervals):
            res = [intervals[0]]
            for i in range(1,len(intervals)):
                current = intervals[i]
                if current[0] < res[-1][1]:
                    res[-1][1] = max(res[-1][1],current[1])
                else:
                    res.append(current)
            return res
    
        char_range = defaultdict(list)
        for idx, char in enumerate(s):
            if char not in char_range:
                char_range[char] = [idx,idx]
            else:
                char_range[char][1] = idx
    
        intervals = list(char_range.values())
        del char_range
        merged = merge_intervals(intervals)
        for idx, val in enumerate(merged):
            merged[idx] = val[1] - val[0] + 1
            
        return merged
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        freq = dict(zip(heights,names))
        maxx = max(heights)
        buckets = [0] *(maxx + 1)
        res = []
        
        for i in heights:
            buckets[i] += 1
            
        for j in range(len(buckets)-1,-1,-1):
            while buckets[j]:
                res.append(freq[j])
                buckets[j] -= 1
                
        return res
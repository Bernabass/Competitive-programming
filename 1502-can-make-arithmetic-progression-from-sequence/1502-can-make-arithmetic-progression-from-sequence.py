class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        _min, n = min(arr), len(arr)
        diff = max(arr) - _min
        if not diff:
            return True
        
        d = diff / (n - 1)
        count = Counter()
        
        for num in arr:
            count[(num - _min) / d] += 1
            
        return all(key in range(n) and val == 1 for key, val in count.items())
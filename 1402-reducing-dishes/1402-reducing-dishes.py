class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        arr, max_val = deque(sorted(satisfaction)), 0
        
        def calc(arr):
            return sum((i+1)*val for i, val in enumerate(arr))
        
        while arr:
            max_val = max(max_val, calc(arr))
            arr.popleft()
            
        return max_val
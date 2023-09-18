class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        max_visited, N = 0, len(arr)
        
        @cache
        def dp(idx):            
            max_gained = 1
            i = j = idx
            
            while i - 1 >= max(0, idx - d) and arr[i - 1] < arr[idx]:
                max_gained = max(max_gained, 1 + dp(i - 1))
                i -= 1
                
            while j + 1 < min(N, idx + d + 1) and arr[j + 1] < arr[idx]:
                max_gained = max(max_gained, 1 + dp(j + 1))
                j += 1
                
            return max_gained
        
        for index in range(len(arr)):
            max_visited = max(max_visited, dp(index))
            
        return max_visited
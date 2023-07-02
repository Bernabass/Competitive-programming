class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        info, max_length = defaultdict(int), 0
        
        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            info[curr] = info[curr + difference] + 1
            max_length = max(max_length, info[curr])
                            
        return max_length
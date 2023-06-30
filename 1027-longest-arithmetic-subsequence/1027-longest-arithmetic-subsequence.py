class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n, max_length = len(nums), 0
        info = defaultdict(lambda:2)
        
        for i in range(n):
            for j in range(i+1, n):
                diff = nums[i] - nums[j]
                info[(diff, j)] = info[(diff, i)] + 1
                
                max_length = max(max_length, info[(diff, i)])
            
        return max_length
                 
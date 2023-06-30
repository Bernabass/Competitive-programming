class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        info = defaultdict(int)
        
        for i in range(n):
            for j in range(i+1, n):
                diff = nums[i] - nums[j]
                info[(diff, j)] = info[(diff, i)] + 1
            
        return max(info.values()) + 1
                 
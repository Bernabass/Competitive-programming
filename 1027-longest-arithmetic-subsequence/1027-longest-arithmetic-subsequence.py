class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        max_length = 0
        dp = {} 
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if (diff, j) in dp:
                    dp[(diff, i)] = dp[(diff, j)] + 1
                else:
                    dp[(diff, i)] = 2
                max_length = max(max_length, dp[(diff, i)])
                
        return max_length

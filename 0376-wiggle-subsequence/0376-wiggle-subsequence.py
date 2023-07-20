class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = defaultdict(list)
        max_len, n = 0, len(nums)
        
        for i in range(n - 1, -1, -1):
            dp[i] = [1, 1]
            for j in range(i + 1, n):
                nxt = dp.get(j, (0, 0))
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], nxt[1] + 1)
                
                if nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], nxt[0] + 1)
                    
            max_len = max(max_len, max(dp[i]))
                  
        return max_len
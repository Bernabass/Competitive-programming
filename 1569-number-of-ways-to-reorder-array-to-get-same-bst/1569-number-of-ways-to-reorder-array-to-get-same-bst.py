class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def dfs(nums):
            if len(nums) < 3: 
                return 1
            left = [val for val in nums if val < nums[0]]
            right = [val for val in nums if val > nums[0]]
            
            return comb(len(nums)-1, len(left)) * dfs(left) * dfs(right)
        
        return (dfs(nums) - 1) % (10 ** 9 + 7) 
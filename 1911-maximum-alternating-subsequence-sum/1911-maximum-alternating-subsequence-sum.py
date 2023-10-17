class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        N = len(nums)
        
        no_pick = pick = 0

        for i in range(N):
            new_no_pick = max(no_pick, pick + nums[i])
            new_pick = max(pick, no_pick - nums[i])
            no_pick, pick = new_no_pick, new_pick

        return max(no_pick, pick)
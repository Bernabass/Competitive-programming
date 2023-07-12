class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float("inf")
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            for j in range(i+1, n-1):
                curr = target - (nums[i] + nums[j])
                idx = bisect_left(nums, curr, j+1)
                valid = nums[idx-1]
                
                if idx < n and (idx == j+1 or abs(curr - nums[idx]) < abs(curr - nums[idx-1])):
                    valid = nums[idx]
                    
                curr_ans = nums[i] + nums[j] + valid
                if abs(ans - target) > abs(curr_ans - target):
                    ans = curr_ans
                
        return ans
                
        
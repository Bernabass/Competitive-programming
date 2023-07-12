class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = inf
        
        for idx in range(n):
            if idx and nums[idx] == nums[idx-1]:
                continue
                
            left, right = idx + 1, n - 1
            
            while left < right:
                curr_sum = nums[idx] + nums[left] + nums[right]
                
                if abs(curr_sum - target) < abs(ans - target):
                    ans = curr_sum

                if curr_sum < target:
                    left += 1
                    
                elif curr_sum > target:
                    right -= 1
                    
                else:
                    return target
                    
        return ans
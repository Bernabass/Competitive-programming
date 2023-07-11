class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, n = [], len(nums)
        nums.sort()
        
        for i in range(n):
            for j in range(i+1, n):
                x = target - nums[i] - nums[j]
                left, right = j+1, n - 1
                
                while left < right:
                    
                    if nums[left] + nums[right] < x:
                        left += 1
                        
                    elif nums[left] + nums[right] > x:
                        right -= 1
                        
                    else:
                        ans.append((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        
        return set(ans)
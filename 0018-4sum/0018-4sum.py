class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, prev = [], []
        n = len(nums)
        nums.sort()
        
        def back_track(idx, target, k):
            if k == 2:
                left, right = idx,  n - 1

                while left < right:

                    if nums[left] + nums[right] < target:
                        left += 1

                    elif nums[left] + nums[right] > target:
                        right -= 1

                    else:
                        ans.append(prev + [nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                            
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
                            
                return
            
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                    
                prev.append(nums[i])
                back_track(i+1, target - nums[i], k - 1)
                prev.pop()
    
        back_track(0, target, 4)
        
        return ans
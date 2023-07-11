class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans, prev = [], []
        n = len(nums)
        nums.sort()
        
        def back_track(idx, target, k):
            if k == 2:
                right = n - 1

                while idx < right:

                    if nums[idx] + nums[right] < target:
                        idx += 1

                    elif nums[idx] + nums[right] > target:
                        right -= 1

                    else:
                        ans.append(prev + [nums[idx], nums[right]])
                        idx += 1
                        while idx < right and nums[idx] == nums[idx-1]:
                            idx += 1
                            
                return
            
            for i in range(idx, n):
                if i > idx and nums[i] == nums[i-1]:
                    continue
                    
                prev.append(nums[i])
                back_track(i+1, target - nums[i], k - 1)
                prev.pop()
    
        back_track(0, target, 4)
        
        return ans
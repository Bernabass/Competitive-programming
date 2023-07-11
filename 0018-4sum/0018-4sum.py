class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                x = target - nums[i] - nums[j]
                pair = self.two_sum(nums[j+1:], x)
                
                if pair:
                    for val in pair:
                        ans.append(tuple(sorted((nums[i], nums[j]) + val)))
                    
        return set(ans)
                    
    def two_sum(self, arr, target):
        info = {}
        ans = []
        for idx, val in enumerate(arr):
            x = target - val
            if x in info:
                ans.append((val, x))
            
            info[val] = idx
                
        return ans
                
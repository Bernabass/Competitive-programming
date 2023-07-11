class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        
        for i in range(n):
            for j in range(i+1, n):
                x = target - nums[i] - nums[j]
                pair = self.two_sum(nums, x, j+1)
                
                if pair:
                    for val in pair:
                        ans.append((nums[i], nums[j]) + val)
                    
        return set(ans)
                    
    def two_sum(self, arr, target, idx):
        ans, seen = [], set()
        for i in range(idx, len(arr)):
            val = arr[i]
            x = target - val
            if x in seen:
                ans.append((x, val))
                
            seen.add(val)
                
        return ans
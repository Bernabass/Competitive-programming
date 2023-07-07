class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        arr = [0]*(max(nums)+1)
        
        for num in nums:
            arr[num] += num
            
        return self.rob(arr)
    
    def rob(self, nums: List[int]) -> int:
        money , n = 0 , len(nums)
        for i in range(n-1, -1, -1):
            curr_max = 0
            if i + 2 < n:
                curr_max = nums[i+2]
            if i + 3 < n:
                curr_max = max(curr_max, nums[i+3])
                
            nums[i] += curr_max
            money = max(nums[i], money)
            
        return money
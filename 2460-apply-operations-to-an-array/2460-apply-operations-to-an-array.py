class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        
        for idx in range(1,n):
            if nums[idx-1] == nums[idx]:
                nums[idx-1] = nums[idx-1]*2
                nums[idx] = 0
         
        count = 0
        for number in nums:
            if number != 0:
                ans[count] = number
                count += 1
                
        return ans
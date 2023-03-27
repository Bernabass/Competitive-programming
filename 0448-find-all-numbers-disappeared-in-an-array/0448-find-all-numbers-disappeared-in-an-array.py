class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for idx in range(n):
            while idx+1 != nums[idx] and nums[nums[idx]-1] != nums[idx]:
                temp = nums[idx]
                nums[idx] = nums[temp-1]
                nums[temp-1] = temp
          
        for idx, val in enumerate(nums):
            if idx+1 != val:
                ans.append(idx+1)
            
        return ans
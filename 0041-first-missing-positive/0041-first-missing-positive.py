class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for idx in range(n):
            while idx + 1  != nums[idx] and 1 <= nums[idx] <= n and nums[nums[idx]-1] != nums[idx]:
                temp = nums[idx]
                nums[idx] = nums[nums[idx]-1]
                nums[temp-1] = temp

        for idx, val in enumerate(nums, 1):
            if idx != val:
                return idx
            
        return n+1
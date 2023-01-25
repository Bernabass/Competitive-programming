class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = k = 0
        for right, val in enumerate(nums):
            if val != nums[left]:
                nums[left+1] = val
                left += 1
                k += 1

        return k +1
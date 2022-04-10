class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            m=nums[i]
            for j in range(i,len(nums)):
                if nums[j]<=m:
                    m=nums[j]
                    idx=j
            nums[idx]=nums[i]
            nums[i]=m



            

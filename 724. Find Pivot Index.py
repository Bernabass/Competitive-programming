class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[:i]==[]:
                sum(nums[:i])==0
            if sum(nums[:i])==sum(nums[i+1:len(nums)]):
                    return i
        else:
            return -1
            
            
        
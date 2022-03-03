class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums=[]
        output=[]
        for i in range(len(nums)):
            sorted_nums.append(min(nums))
            if sorted_nums[i]==target:
                output.append(i)
            nums.remove(min(nums))
        return output
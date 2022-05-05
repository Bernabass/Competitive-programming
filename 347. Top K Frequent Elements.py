class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()
        new=list(set(nums))
        new.sort()
        count=[1]
        output=[]
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                count[-1]+=1
            else:
                count.append(1)
        lis=list(zip(count,new))
        lis.sort(reverse=True)
        for j in range(k):
            output.append(lis[j][1])
        return (output)
        
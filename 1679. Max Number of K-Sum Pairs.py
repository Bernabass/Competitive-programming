class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic=Counter(nums) 
        c=0
        for i in range(len(nums)):
            if k-nums[i] in dic and (dic[k-nums[i]] and dic[nums[i]]>0):
                if k-nums[i]==nums[i] and (dic[nums[i]]//2)>0 or k-nums[i]!=nums[i] :
                    c+=1
                    dic[nums[i]]-=1
                    dic[k-nums[i]]-=1 
        return c

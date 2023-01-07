class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = dict(zip(nums,range(len(nums))))
        res = [0] * len(nums)
        
        for i, j in operations:
            dic[j] = dic[i]
            del dic[i]

        for i, j in dic.items():
            res[j] += i
            
        return res

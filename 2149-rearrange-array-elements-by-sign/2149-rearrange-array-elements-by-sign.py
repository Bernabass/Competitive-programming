class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives, negatives, res = [], [], []
        count, n = 0, len(nums)//2
        for i in nums:
            if i < 0:
                negatives.append(i)
            else:
                positives.append(i)
                
        while count < n:
            res.append(positives[count])
            res.append(negatives[count])
            count += 1
            
        return res
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        query = queries[0]
        nums[query[1]] += query[0]
        current = 0
        res = []
        for i in nums:
            if i % 2 == 0 :
                current += i
        res.append(current)
    
        for query in queries[1:]:
            idx , val = query[1] , query[0]
            if nums[idx] % 2 == 0 :
                current -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0 :
                current += nums[idx]
            res.append(current)
        
        return res          
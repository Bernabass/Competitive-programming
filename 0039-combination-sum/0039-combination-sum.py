class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def helper(nums, nextt, target, partial, ans):
            if not target:
                ans.append(partial)
                return
            if nextt == len(nums):
                return 
            
            count = 0
            
            while target - count*nums[nextt] >= 0:
                helper(nums, nextt + 1, target - count*nums[nextt], partial + [nums[nextt]]*count, ans )
                count += 1
                
        helper(candidates, 0, target, [], ans)
        
        return ans
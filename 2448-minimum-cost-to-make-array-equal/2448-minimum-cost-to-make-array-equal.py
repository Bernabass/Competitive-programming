class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        left, right = min(nums), max(nums)
        
        def total_cost(target):
            return sum(abs(target - num)*val for num, val in zip(nums, cost))
        
        while left < right:
            mid = (left + right) // 2
            
            if total_cost(mid) < total_cost(mid + 1):
                right = mid
                
            else:
                left = mid + 1
        
        return total_cost(left)
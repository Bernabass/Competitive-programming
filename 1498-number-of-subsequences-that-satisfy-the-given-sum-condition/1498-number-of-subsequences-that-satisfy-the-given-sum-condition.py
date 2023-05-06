class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        start, end = 0, len(nums) - 1
        count, mod = 0, 10**9 + 7
        nums.sort()
        
        while start <= end:
            if nums[start] + nums[end] <= target:
                count += 2**(end-start) % mod
                start += 1
                
            else:
                end -= 1
                
        return count % mod
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = left = max_ones = 0
        
        
        for right in range(len(nums)):
            if not nums[right]:
                zeros += 1
                
            while zeros > k:
                if not nums[left]:
                    zeros -= 1
                    
                left += 1
                
            max_ones = max(max_ones, right - left + 1)
            
        
        return max_ones
        
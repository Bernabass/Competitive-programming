class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = max_size = zeros = 0
        wereZeros = False
        
        for right in range(len(nums)):
            if not nums[right]:
                wereZeros = True
                zeros += 1
                
            while zeros > 1:
                if not nums[left]:
                    zeros -= 1
                    
                left += 1
                
            max_size = max(max_size, right - left + 1 - zeros)
            
        
        if not wereZeros:
            max_size -= 1
        
        return max_size
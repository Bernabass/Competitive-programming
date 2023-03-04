class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = ans = 0
        previous_prefix_sums = defaultdict(int)
        previous_prefix_sums[0] += 1
        
        for num in nums:
            prefix_sum += num
            
            if prefix_sum - k in previous_prefix_sums:
                ans += previous_prefix_sums[prefix_sum - k]
                
            previous_prefix_sums[prefix_sum] += 1
            
        return ans
        
        
        
        
        """ if nums[i] > 0, This code will work"""
#         n = len(nums)
#         ptr = left = window_sum = count = 0
#         nums.append(1)
#         last_valid_zero = defaultdict(int)
        
        
#         for i in range(n):
#             if ptr < i:
#                 ptr = i
#             while ptr < n and (not nums[ptr + 1]):
#                 ptr += 1

#             last_valid_zero[i] += ptr
                    
        
#         for right in range(n):
#             window_sum += nums[right]
            
#             while window_sum >= k and left <= right:
#                 if window_sum == k:
#                     count += last_valid_zero[right] - right + 1
                    
#                 window_sum -= nums[left]
#                 left += 1   
                
        # return count
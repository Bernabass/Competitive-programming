class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = ans = 0
        prev_prefix_modes = defaultdict(int)
        prev_prefix_modes[0] += 1
        
        for num in nums:
            prefix_sum += num
            
            if prefix_sum % k in prev_prefix_modes:
                ans += prev_prefix_modes[prefix_sum % k]
                
            prev_prefix_modes[prefix_sum % k] += 1
            
            
        return ans
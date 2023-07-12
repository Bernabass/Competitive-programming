class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        prev_prefix_rem = defaultdict(int)
        prev_prefix_rem[0] = -1
        
        for idx, num in enumerate(nums):
            prefix_sum += num
            curr_rem = prefix_sum % k
            
            if curr_rem in prev_prefix_rem:
                if idx - prev_prefix_rem[curr_rem] > 1:
                    return True
            
            else:
                prev_prefix_rem[curr_rem] = idx
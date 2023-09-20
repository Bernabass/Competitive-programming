class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        cum_sum = [0]
        curr_sum = 0
        for num in nums:
            curr_sum += num
            cum_sum.append(curr_sum)
            
        sum_to_idx = {v: i for i, v in enumerate(cum_sum)}
        max_len = -1
        for l_val, l_idx in sum_to_idx.items():
            if l_val + target in sum_to_idx:
                max_len = max(sum_to_idx[l_val + target] - l_idx, max_len)
                
        return n - max_len if max_len != -1 else -1

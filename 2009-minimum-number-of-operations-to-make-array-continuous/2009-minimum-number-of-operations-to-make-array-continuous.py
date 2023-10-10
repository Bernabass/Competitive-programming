class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        nums = sorted(set(nums))
        ans = float('inf')

        for idx, start in enumerate(nums):
            end = start + N - 1
            curr = bisect_right(nums, end)

            ans = min(ans, N - (curr - idx))
            
        return ans
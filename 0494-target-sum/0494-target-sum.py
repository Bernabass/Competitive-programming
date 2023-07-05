class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def back_track(idx, prev_sum):
            if idx == len(nums):
                return prev_sum == target

            if (idx, prev_sum) in memo:
                return memo[(idx, prev_sum)]

            add = back_track(idx+1, prev_sum + nums[idx])
            subtract = back_track(idx+1, prev_sum - nums[idx])

            memo[(idx, prev_sum)] = add + subtract
            return add + subtract

        return back_track(0, 0)
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        ans = float("inf")
        right = k - 1
        while right < n:
            ans = min(ans,nums[right] - nums[left])
            left += 1
            right += 1
        return ans
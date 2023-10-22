class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = window_min = nums[k]
        left, right, n = k, k, len(nums)

        while left or right < n - 1:
            
            if not left or (right < n - 1 and nums[left - 1] < nums[right + 1]):
                right += 1
                window_min = min(window_min, nums[right])
                
            else:
                left -= 1
                window_min = min(window_min, nums[left])

            ans = max(ans, window_min * (right - left + 1))

        return ans
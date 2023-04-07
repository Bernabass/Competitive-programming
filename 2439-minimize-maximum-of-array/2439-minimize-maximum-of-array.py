class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = min(nums), max(nums)

        def is_possible(median):
            count = 0
            for i in range(n-1, -1, -1):
                if nums[i] > median:
                    count += nums[i] - median
                else:
                    if nums[i] + count > median:
                        count = nums[i] + count - median
                    else:
                        count = 0
            return count == 0


        res = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
 
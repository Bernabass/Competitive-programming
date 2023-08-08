class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(arr, target, left, right):
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                elif arr[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        low = 0
        high = len(nums) - 1
        zeroth = nums[0]
        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= zeroth:
                low = mid + 1
            else:
                high = mid

        if nums[low] < zeroth:
            if zeroth <= target <= nums[low - 1]:
                return binary_search(nums, target, 0, low - 1)
            else:
                return binary_search(nums, target, low, len(nums) - 1)
        else:
            return binary_search(nums, target, 0, len(nums) - 1)

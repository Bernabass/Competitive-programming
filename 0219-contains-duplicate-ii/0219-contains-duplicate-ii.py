class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = right = size = 0
        n = len(nums)
        
        while right < n:
            if size > k:
                window.remove(nums[left])
                left += 1
                size -= 1
            if nums[right] in window:
                return True
            window.add(nums[right])
            size += 1
            right += 1
        
        return False
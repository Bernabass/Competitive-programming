class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]

        def valid(mid):
            count = i = 0

            while count < p and i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
                    
            return count >= p

        while left < right:
            mid = (left + right) // 2
            
            if valid(mid):
                right = mid
                
            else:
                left = mid + 1

        return left
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        start = operations = 0
        end = N - 1
        
        while start < end:
            if nums[start] + nums[end] > k:
                end -= 1
                
            elif nums[start] + nums[end] < k:
                start += 1
                
            else:
                operations += 1
                start += 1
                end -= 1
                
        return operations
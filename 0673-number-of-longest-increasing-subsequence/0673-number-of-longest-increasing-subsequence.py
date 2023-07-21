class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        length = [1] * n
        count  = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j]:
                        length[i] = length[j]+1
                        count[i]  = count[j]
                    elif length[i] == length[j]+1:
                        count[i] += count[j]

        maxLength = max(length)
        
        return sum([count[i] for i in range(n) if length[i] == maxLength])
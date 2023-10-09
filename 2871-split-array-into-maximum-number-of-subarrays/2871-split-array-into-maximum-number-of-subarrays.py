class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        min_score = ~(0)
        count = 0
        info = defaultdict(lambda: True)
        
        for i in range(N):
            min_score &= nums[i]
            
        if min_score:
            return 1
        
        running_AND = ~(0)
        for i in range(N - 1, -1, -1):
            running_AND &= nums[i]
            info[i] = (running_AND == 0)
            
        running_AND = ~(0)

        for right in range(N):
            running_AND &= nums[right]
            if not (running_AND) and info[right + 1]:
                count += 1
                running_AND = ~(0)
                    
        return count
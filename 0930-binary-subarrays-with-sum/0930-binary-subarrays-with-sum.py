class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        window_sum = left = count = 0
        next_one = defaultdict(int)

        last = n
        for i in range(len(nums) - 1, -1, -1):
            next_one[i] = last
            if nums[i] == 1:
                last = i
        
        
        for right in range(n):
            window_sum += nums[right]
            
            while window_sum >= goal and left <= right:
                if window_sum == goal:
                    count += next_one[right] - right
                window_sum -= nums[left]
                
                left += 1
            
        
        return count
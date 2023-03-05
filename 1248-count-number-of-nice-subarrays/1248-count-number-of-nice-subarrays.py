class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ptr = left = window_sum = count = 0
        nums.append(1)
        last_valid_even = defaultdict(int)
        
        
        for i in range(n):
            if ptr < i:
                ptr = i
            while ptr < n and (not nums[ptr + 1] % 2):
                ptr += 1

            last_valid_even[i] += ptr
           
        for right in range(n):
            if nums[right] % 2:
                window_sum += 1
            
            while window_sum >= k and left <= right:
                if window_sum == k:
                    count += last_valid_even[right] - right + 1
                 
                if nums[left] % 2:
                    window_sum -= 1
                left += 1   
                
        return count
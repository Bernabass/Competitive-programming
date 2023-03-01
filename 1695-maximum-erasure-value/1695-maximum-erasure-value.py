class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        uniques = defaultdict(int)
        left = max_score = window_score = 0
        
        for right in range(len(nums)):
            uniques[nums[right]] += 1
            window_size = right - left + 1
            window_score += nums[right]
            
            while window_size > len(uniques):
                
                uniques[nums[left]] -= 1
                window_score -= nums[left]
            
                if not uniques[nums[left]]:
                    del uniques[nums[left]]
                    
                left += 1
                window_size -= 1
                
                
            max_score = max(max_score, window_score)
            
            
        return max_score
            
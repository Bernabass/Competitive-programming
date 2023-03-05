class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_odd = nice_subArrays = 0
        prev_prefix_odds = defaultdict(int)
        prev_prefix_odds[0] += 1
        
        for num in nums:
            prefix_odd += num % 2
            if prefix_odd - k in prev_prefix_odds:
                nice_subArrays += prev_prefix_odds[prefix_odd - k]
                
            prev_prefix_odds[prefix_odd] += 1
            
        return nice_subArrays
                                  
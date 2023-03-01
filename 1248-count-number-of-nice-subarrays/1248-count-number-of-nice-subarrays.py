class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_odds = [0]*len(nums)
        nice_subArrays = 0
        
        for idx, num in enumerate(nums):
            prefix_odds[idx] = prefix_odds[idx-1] + num % 2
                
        freq = Counter(prefix_odds)
        freq[0] = freq.get(0,0) + 1

        
        for each in prefix_odds:
            if (each - k) in freq:
                nice_subArrays += freq[each - k]
                
        return nice_subArrays
                
                                  
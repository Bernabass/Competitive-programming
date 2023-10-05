class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        
        ans = [key for key, val in freq.items() if val > len(nums) // 3]
        
        return ans
    
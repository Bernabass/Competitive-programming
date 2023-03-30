class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq = list(zip(freq.values(), freq.keys()))
        freq.sort(reverse = True)
        ans = []
        
        for _ in range(k):
            ans.append(freq[_][1])
            
        return ans
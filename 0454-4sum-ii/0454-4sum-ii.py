class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        pair_sum1 = defaultdict(int)
        pair_sum2 = defaultdict(int)
        n, count = len(nums1), 0
        
        for i in range(n):
            for j in range(n):
                pair_sum1[nums1[i] + nums2[j]] += 1
                pair_sum2[nums3[i] + nums4[j]] += 1
        
        for sum1, freq1 in pair_sum1.items():
            count += pair_sum2[-sum1] * freq1
                    
        return count
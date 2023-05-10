class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(val + nums2[0], val, 0) for val in nums1[:k]]
        limit = min(k, len(nums1) * len(nums2))
        ans = []

        for _ in range(limit):    
            curr_sum, val, v = heappop(heap)
            ans.append([val, nums2[v]])
            
            if v < len(nums2) - 1:
                heappush(heap, (val + nums2[v+1], val, v+1))

        return ans
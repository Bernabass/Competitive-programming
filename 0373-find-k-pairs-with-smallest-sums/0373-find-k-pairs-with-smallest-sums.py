class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(val + nums2[0], idx, 0) for idx, val in enumerate(nums1[:k])]
        limit = min(k, len(nums1) * len(nums2))
        ans = []

        for _ in range(limit):    
            curr_sum, u, v = heappop(heap)
            ans.append([nums1[u], nums2[v]])
            
            if v < len(nums2) - 1:
                heappush(heap, (nums1[u] + nums2[v+1], u, v+1))

        return ans
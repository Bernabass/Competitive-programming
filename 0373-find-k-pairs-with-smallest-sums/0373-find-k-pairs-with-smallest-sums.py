class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(n1 + nums2[0], n1, 0) for n1 in nums1[:k]]
        ans = []

        for _ in range(min(k, len(nums1) * len(nums2))):    
            sm, n1, n2_idx = heappop(heap)
            ans.append([n1, nums2[n2_idx]])
            if n2_idx < len(nums2) - 1:
                heappush(heap, (n1 + nums2[n2_idx + 1], n1, n2_idx + 1))

        return ans

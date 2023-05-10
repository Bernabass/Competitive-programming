class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        arr = [(val + nums2[0], idx, 0) for idx, val in enumerate(nums1)]
        ans = []
        heapify(arr)
        
        while arr and len(ans) < k:
            Sum, u, v = heappop(arr)
            ans.append([nums1[u], nums2[v]])
            
            if v < len(nums2) - 1:
                curr_sum = nums1[u] + nums2[v+1]
                heappush(arr, (curr_sum, u, v+1))
                
        return ans
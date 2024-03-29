class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N1, N2 = len(nums1), len(nums2)
        
        @cache
        def dp(i, j):
            if i == N1 or j == N2:
                return -inf
            
            
            pick = dp(i + 1, j + 1)
            no_pick = max(dp(i + 1, j), dp(i, j + 1))
            
            return max(nums1[i] * nums2[j] + max(0, pick), no_pick)
        
        
        return dp(0, 0)
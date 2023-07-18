class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = defaultdict(int)
        max_len = 0
        
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1 , -1):
                if nums1[i] == nums2[j]:
                    dp[(i, j)] = 1 + dp[(i + 1, j + 1)]
                    
                max_len = max(max_len, dp[(i, j)])
                
        return max_len
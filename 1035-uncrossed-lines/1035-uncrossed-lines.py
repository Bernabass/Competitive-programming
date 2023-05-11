class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dic = defaultdict(list)
        for i,num in enumerate(nums2):
            dic[num].append(i)
        
        @lru_cache(None)
        def rec(i=0, i_max=-1):

            if i==n:
                return 0
            
            num = nums1[i]
            i2 = bisect_left(dic[num], i_max+1)
            if i2<len(dic[num]):
                return max(1+rec(i+1, dic[num][i2]), rec(i+1, i_max))
            
            return rec(i+1, i_max)
        
        return rec()
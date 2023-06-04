class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ans = []
        for val in nums:
            idx = bisect.bisect_left(ans, val)
            if idx == len(ans):
                if idx == 2:
                    return True
                ans.append(val)
            else:
                ans[idx] = val
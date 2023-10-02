class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        @cache
        def back_track(oper, arr):
            if not arr:
                return 0
            
            ans = 0
            arr = list(arr)
            for i in range(len(arr)):
                first = arr[i]
                for j in range(i + 1, len(arr)):
                    second = arr[j]
                    arr.remove(first)
                    arr.remove(second)
                    ans = max(ans, oper * gcd(first, second) + back_track(oper + 1, tuple(arr)))
                    arr.insert(i, first)
                    arr.insert(j, second)
                
            return ans
        
        return back_track(1, tuple(nums))
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def f(x):
            start = max(0, index - (x - 1))
            end = min(n - 1, index + (x - 1))
            front_ans = (x - (index - start) + x - 1) * (index - start) // 2
            back_ans = (x - 1 + x - (end - index)) * (end - index) // 2
            return front_ans + back_ans + x + (start - 0) + (n-1-end)
        
        def bisect_right(left, right):
            while left <= right:
                mid = (left + right) >> 1
                if f(mid) > maxSum:
                    right = mid - 1
                else:
                    left = mid + 1
            return right
        
        return bisect_right(1, maxSum)
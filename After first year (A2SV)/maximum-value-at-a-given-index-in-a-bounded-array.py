class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def do(val):
            start = max(0, index - (val - 1))
            end = min(n - 1, index + (val - 1))
            front = (val - (index - start) + val - 1) * (index - start) // 2
            back = (val - 1 + val - (end - index)) * (end - index) // 2

            return front + back + val + (start + n - 1 - end)
        
        left, right = 1, maxSum
        while left <= right:
            mid = (left + right) // 2

            if do(mid) > maxSum:
                right = mid - 1

            else:
                left = mid + 1

        return right
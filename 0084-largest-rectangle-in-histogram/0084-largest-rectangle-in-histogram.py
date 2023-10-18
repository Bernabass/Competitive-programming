class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        max_area = max(heights)
        
        def nearest_smaller(arr):
            res = [-1] * N
            stack = []
            for i in range(N):
                while stack and arr[stack[-1]] > arr[i]:
                    res[stack.pop()] = i
                stack.append(i)

            return res
        
        prev_smallers = nearest_smaller(heights[::-1])[::-1]
        next_smallers = nearest_smaller(heights)   
        
        for idx, val in enumerate(heights):
            left = -1 if prev_smallers[idx] == -1 else  N - prev_smallers[idx] - 1
            right = next_smallers[idx] if next_smallers[idx] != -1 else N

            max_area = max(max_area, val * (right - left - 1))
            
        return max_area
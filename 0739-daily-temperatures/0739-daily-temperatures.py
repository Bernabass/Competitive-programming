class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack , result = [] , n*[0]
        for i in range(1,n):
            if temperatures[i] > temperatures[i-1]:
                result[i-1] = 1
                while stack and temperatures[i] >temperatures[stack[-1]]:
                    p = stack.pop()
                    result[p] = i - p
            else:
                stack.append(i-1)
        return result
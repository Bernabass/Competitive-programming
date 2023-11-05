class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        result = [n] * n
        stack = []

        for i in range(n):
            while stack and arr[i] > arr[stack[-1]]:
                result[stack[-1]] = i
                stack.pop()

            stack.append(i)

        prev_max = arr[0]
        for idx, num in enumerate(result):
            val = num - idx - 1 + (arr[idx] > prev_max)
            if val >= k:
                return arr[idx]

            prev_max = max(prev_max, num)

        return max(arr)
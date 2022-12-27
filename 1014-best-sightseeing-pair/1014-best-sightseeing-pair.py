class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = values[1] + values[0] - 1
        maxx = 0
        for i in range(1,len(values)):
            current = values[i] + values[i-1] - 1
            temp = values[i] + values[maxx] + (maxx - i)
            if temp > current:
                best = max(temp,best)
            else:
                best = max(best,current)
            if values[i] + i - maxx >= values[maxx]:
                maxx = i
        return best
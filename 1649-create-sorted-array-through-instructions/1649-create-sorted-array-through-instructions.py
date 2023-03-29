class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        ans = []
        cost = 0
        
        for num in instructions:
            a = len(ans) - bisect_right(ans, num)
            b = bisect_right(ans, num-1)
            cost += min(a, b)
            cost %= 10 ** 9 + 7
            bisect.insort(ans, num)
            
        return cost
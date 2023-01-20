class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        maxx = 0
        for i in range(n):
            for j in range(i+1,n):
                if colors[i] != colors[j]:
                    maxx = max(maxx,j-i)
                    
                    
        return maxx         
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m , n , atlantic , pacific= len(heights),len(heights[0]) , set() , set()
        neighbours = [[1,0],[-1,0],[0,1],[0,-1]]
        result = []
        for i in range(m):
            atlantic.add((i,n-1))
            pacific.add((i,0))
        for j in range(n):
            atlantic.add((m-1,j))
            pacific.add((0,j)) 
        for total in [atlantic,pacific]:
            level = set(total)
            while level:
                levelX = set()
                for i,j in level:
                    for r,c in neighbours:
                        if i+r < 0 or i+r >= m or j+c < 0 or j+c >= n or (i+r,j+c) in total:
                            continue
                        if heights[i+r][j+c] >= heights[i][j]:
                            levelX.add((i+r,j+c))
                    
                level = levelX
                total |= (levelX)
        return list(atlantic.intersection(pacific))
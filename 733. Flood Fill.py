class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = [[sr,sc]]
        starting_pixel = image[sr][sc]
        image[sr][sc] = color
        visited = set([sr,sc])
        while queue:
            p = queue.pop()
            for x,y in [[0,1],[1,0],[0,-1],[-1,0]]:
                if 0 <= p[0] + x < len(image) and 0 <= p[1] + y < len(image[0]):
                    neighbour = (p[0]+x,p[1]+y)
                    if neighbour not in visited and image[neighbour[0]][neighbour[1]] == starting_pixel:
                        queue.append(neighbour)
                        visited.add(neighbour)
                        image[neighbour[0]][neighbour[1]] = color
        return image
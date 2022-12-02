image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
queue = [(sr,sc)]
image[sr][sc] = color
visited = set([sr,sc])
while queue:
    p = queue.pop()
    print(p)
    for x,y in [[0,1],[1,0],[0,-1],[-1,0]]:
        temp = (p[0]+x,p[1]+y)
        print(temp)
        if temp not in visited:
            queue.append(temp)
            visited.add(temp)
            image[p[0]+x][p[1]+y] = color
print(image)
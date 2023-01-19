m, n = list(map(int,input().split()))
grid = []
res = []

for r in range(m):
    row = list(input())
    grid.append(row)

def traverse(i,j):
    original = grid[i][j][-1]
    count = 1

    while i + count < m:
        if grid[i+count][j][-1] == original:
            grid[i+count][j] = grid[i][j]  = "1" + original

        count += 1

    count = 1
    while j + count < n:
        if grid[i][j+count][-1] == original:
            grid[i][j+count] = grid[i][j]  = "1" + original

        count += 1

for row in range(m):
    for col in range(n):
        traverse(row,col)
        if grid[row][col].isalpha():
            res.append(grid[row][col])

print("".join(res))

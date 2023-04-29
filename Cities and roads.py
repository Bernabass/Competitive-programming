n = int(input())
roads = 0
seen = set()

for row in range(n):
    inp = map(int, input().split())
    
    for col, val in enumerate(inp):
        if val and (row, col) not in seen:
            roads += 1
            seen.add((row, col))
            seen.add((col, row))
            
print(roads)
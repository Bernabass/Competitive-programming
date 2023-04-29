n = int(input())

for _ in range(n):
    row = map(int, input().split())
    ans = []
    
    for col, val in enumerate(row):
        if val:
            ans.append(str(col+1))
            
    print(len(ans), " ".join(ans))
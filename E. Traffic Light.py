t = int(input())
for _ in range(t):
    c = input().split()
    start = c[1]
    s = input()
    new = s + s
    count = 0
    left = 0
    right = 0
    out = 0
    while :
        if s[left] != start:
            left += 1
            right +=1
        else:
            

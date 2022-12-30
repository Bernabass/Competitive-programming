t = int(input())
for _ in range(t):
    c = input().split()
    start = c[1]
    s = input()
    new = s + s
    count = 0
    left , right = 0 , 0
    while left < len(s):
        if new[left] != start:
            left += 1
            right += 1
        else:
            while new[right] != "g":
                right += 1
            count = max(count, right - left)
            left , right  = right + 1 , right + 1
    print(count)
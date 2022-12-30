from collections import Counter
t = int(input())
for _ in range(t):
    inp = list(map(int,input().split()))
    n , c = inp[0], inp[1]
    orbits = list(map(int,input().split()))
    info = Counter(orbits)
    cost = 0

    for planet in info:
        if info[planet] >= c:
            cost += c
        else:
            cost += info[planet]

    print(cost)
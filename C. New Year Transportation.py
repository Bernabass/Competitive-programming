n,t = list(int(x) for x in input().split())
t-=1
portals = list(int(x) for x in input().split())
portals.append(0)
count=0
while(n-1>count):
    count= count+portals[count]
    if count == t:
        print("YES")
        break
else:
    print("NO")
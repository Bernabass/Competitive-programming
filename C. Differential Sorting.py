t=int(input())
while t>0:
    n=int(input())
    arr=list(map(int,input().split(' ')))
    flag= True
    temp=zip(arr,sorted(arr))
    for i,j in temp:
        if i is not j:
            flag=False
            break
    if flag:
        print(0)
        continue
    if arr[-1]<arr[-2]:
        print(-1)
        continue
    if arr[-1]<0:
        print(-1)
        continue
    print(n-2)
    for i in range(n-2,0,-1):
        print(i, " ", i+1, " ",n)
    t-=1
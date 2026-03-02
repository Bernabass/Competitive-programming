from collections import Counter
abce = 0
for _ in range(int(input())):
    n,l,r=list(map(int,input().split()));a=list(map(int,input().split()))
    count=n//2;x=abs(l-r)//2;c=Counter(a[:l]);d=Counter(a[l:]);z=0
    if l>r:l,r=r,l;c,d=d,c
    for i in c:m=min(c[i],d[i]);d[i]-=m;count-=m
    for i in d:z+=d[i]//2
    print(count+(x-min(x,z)))
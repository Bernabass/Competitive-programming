t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    out=''
    first='a'
    last='z'
    for j in s:
        if k>=ord(j)-ord('a'):
            first=max(first,j)
        else:
            next=j
            k=ord(last)-k-ord('a')
            break
    for l in s:
        if first>=l:
            out+='a'
        elif last>=l and l>chr(ord(first)+k):
            out+=chr(ord(first)+k)
        else:
            out+=l
    print(out)
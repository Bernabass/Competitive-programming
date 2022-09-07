t=int(input())

for i in range(t):
    n,m = map(int, input().split())
    out=[]

    for j in range(n):
        out.append(list(input()))

    for k in range(m):
        check=[]
        for l in range(n):
            if out[l][k]=='o':
                check.append([out[l][k],l])
                out[l][k]="."
            elif out[l][k]=='*':
                check.append([out[l][k]])
                out[l][k]="."
        position=-1

        while check!=[] and position>=-n:
            val=check.pop()
            if val[0]=='*':
                out[position][k]='*'
                position-=1
            elif val[0]=='o':
                out[val[1]][k]='o'
                position=(val[1]-n)-1

    for m in out:
        print("".join(m))
    print()
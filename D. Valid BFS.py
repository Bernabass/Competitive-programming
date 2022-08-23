n=int(input())
tree=[]
for i in range(n+1):
    tree.append(set())
count=1
while count<n:
    x,y=map(int, input().strip().split())
    tree[x].add(y)
    tree[x].add(y)
    count+=1
sequence=list(map(int,input().strip().split()))
i=1
j=0
while i<n and j<n:
    if sequence[i] in tree[sequence[j]]:
        i+=1
    else:
        j+=1
if i==n and sequence[0]==1:
    print("Yes")
else:
    print("No")
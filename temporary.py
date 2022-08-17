grid = [[3,2],[1,0]]
count=0
n=len(grid[0])
for i in grid:
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        print(low,high,mid,count,i)
        if high==low==mid and i[mid]<0:
            negatives=n-mid
            count+=negatives
            break
        elif i[mid]>=0:
            low=mid+1
        else:
            high=mid
    low=0
    high=n-1
print(count)
N, k = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
arr.append(float('inf'))

if not k :
    if arr[0] == 1:
        print(-1)
    else:
        print(1)

elif arr[k-1] != arr[k]:
    print(arr[k-1])

else:
    print(-1)
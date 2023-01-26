t = int(input())

for _ in range(t):
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()

    for idx in range(1, N):
        if abs(arr[idx] - arr[idx-1]) > 1:
            print('NO')
            break

    else:
        print("YES")
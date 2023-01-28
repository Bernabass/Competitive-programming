N = int(input())
arr = list(map(int,input().split()))
odd = even = 0

for num in arr:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

if even and odd:
    arr.sort()
    arr = list(map(str,arr))
    print(" ".join(arr))

else:
    arr = list(map(str,arr))
    print(" ".join(arr))
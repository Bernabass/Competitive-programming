from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    nums = input().split()
    s = input()
    check = defaultdict()
    for i in nums:
        check[i] = str(i)

    idx = 0
    while idx < n:
        if check[nums[idx]].isnumeric():
            check[nums[idx]] = s[idx]
        elif check[nums[idx]] != s[idx]:
            print("NO")
            break
        idx += 1
    else:
        print("YES")
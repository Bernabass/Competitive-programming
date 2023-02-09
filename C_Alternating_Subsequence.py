t = int(input())
for _ in range(t):
    n, arr = int(input()), list(map(int,input().split()))
    stack = [arr[0]]

    for i in range(1, n):
        if arr[i] * stack[-1] > 0:
            if arr[i] > stack[-1]:
                stack.pop()
                stack.append(arr[i])
        else:
            stack.append(arr[i])

    print(sum(stack))
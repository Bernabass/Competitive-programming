t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2:
        if n > 1:
            print(1)
        else:
            print(3)
    else:
        if not (n & (n - 1)):
            print(n + 1)
        else:
            print(n & ~(n - 1))
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    n = int(input())
    left = 0
    right = n - 1
    length = list(map(int,input().split()))
    current = float('inf')
    while left <= right:
        if length[right] <= current:
            if length[right] >= length[left]: 
                current = length[right] 
                right -= 1
            else:
                current = length[left]
                left += 1
        else:
            if length[left] <= current:
                current = length[left]
                left += 1
            else:
                print('No')
                exit()
    print('Yes')
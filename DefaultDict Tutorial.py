# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
inp = list(map(int,input().split()))
n , m = inp[0] , inp[1]
A = defaultdict(list)
B = []
for i in range(n):
    A[input()].append(str(i + 1))
for j in range(m):
    groupB = input()
    if groupB in A:
        print(" ".join(A[groupB]))
    else:
        print("-1")
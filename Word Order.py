# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n = int(input())
col = defaultdict(int)
inp = set()
unique = []
for i in range(n):
    a = input()
    if a not in inp:
        unique.append(a)
    inp.add(a)
    col[a] += 1
print(len(col))
for j in unique:
    print(col[j],end = " ")
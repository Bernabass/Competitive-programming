from collections import defaultdict

n, k = int(input()), int(input())
GRAPH = defaultdict(list)

for _ in range(k):
    operation = input().split()
    if operation[0] == "1":
        GRAPH[operation[1]].append(operation[2])
        GRAPH[operation[2]].append(operation[1])
        
    else:
        print(" ".join(GRAPH[operation[1]]))
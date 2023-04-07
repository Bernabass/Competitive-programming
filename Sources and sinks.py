n = int(input())
graph = [[0] * n for i in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    graph[i] = row
    
sources = []
sinks = []

for i in range(n):
    if sum(graph[i]) == 0:
        sinks.append(i + 1)
    if sum([row[i] for row in graph]) == 0:
        sources.append(i + 1)

print(len(sources), " ".join(map(str, sources)))
print(len(sinks), " ".join(map(str, sinks)))
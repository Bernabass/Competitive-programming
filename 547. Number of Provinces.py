class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = {i:[] for i in range(n)}
        visited = set()
        province = 0
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        for j in graph:
            if j not in visited:
                province += 1
                queue = deque([j])
                while queue:
                    p = queue.popleft()
                    if p not in visited:
                        queue.extend(graph[p])
                        visited.update([p])
        return province
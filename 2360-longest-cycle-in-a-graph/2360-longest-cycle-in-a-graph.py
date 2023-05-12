class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False]*n
        indegree = [0]*n

        for edge in edges:
            if edge != -1:
                indegree[edge] += 1
        
        q = collections.deque()
        for i in range(n):
            if not indegree[i]:
                q.append(i)

        while q:
            node = q.popleft()
            visited[node] = True
            neighbor = edges[node]
            if neighbor != -1:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        ans = -1
        for i in range(n):
            if not visited[i]:
                neighbor = edges[i]
                count = 1
                visited[i] = True

                while neighbor != i:
                    visited[neighbor] = True
                    count += 1
                    neighbor = edges[neighbor]
                ans = max(ans, count)
        return ans
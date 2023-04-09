class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        incomings = [0] * n
        graph = [[] for _ in range(n)]
        counts = [[0] * 26 for _ in range(n)]

        for src, dest in edges:
            incomings[dest] += 1
            graph[src].append(dest)

        sources = [node for node in range(n) if incomings[node] == 0]

        while sources:
            node = sources.pop()
            counts[node][ord(colors[node]) - ord('a')] += 1
            
            for adj in graph[node]:
                counts[adj] = list(map(max, counts[adj], counts[node]))
                incomings[adj] -= 1
                
                if incomings[adj] == 0:
                    sources.append(adj)

        if sum(incomings) > 0:
            return -1
        
        else:
            return max(max(node) for node in counts)

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        GRAPH = defaultdict(list)
        answer = [set() for _ in range(n)]

        for src, dest in edges:
            GRAPH[dest].append(src)

        def bfs(node):
            queue, seen = deque([node]), 1 << node

            while queue:
                curr = queue.popleft()

                for adj in GRAPH[curr]:
                    if not seen & (1 << adj):
                        answer[node].add(adj)
                        seen |= 1 << adj

                        if answer[adj]:
                            answer[node] |= answer[adj]

                        else:
                            queue.append(adj)

        for node in range(n):
            bfs(node)
            
        return map(sorted, answer)
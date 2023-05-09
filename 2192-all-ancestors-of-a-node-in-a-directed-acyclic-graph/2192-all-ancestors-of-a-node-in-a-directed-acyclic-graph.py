class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        GRAPH = defaultdict(list)
        answer = [set() for _ in range(n)]

        for src, dest in edges:
            GRAPH[dest].append(src)

        def bfs(node):
            level, seen = [node], 1 << node

            while level:
                next_level = []

                for curr in level:
                    for adj in GRAPH[curr]:
                        if not seen & (1 << adj):
                            answer[node].add(adj)
                            seen |= 1 << adj
                            answer[node] |= answer[adj]
                            next_level.append(adj)

                level = next_level

        for node in range(n):
            bfs(node)
            
        return map(sorted, answer)
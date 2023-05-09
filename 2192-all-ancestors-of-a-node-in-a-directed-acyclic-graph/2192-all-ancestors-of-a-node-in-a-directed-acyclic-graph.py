class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        GRAPH = defaultdict(list)
        answer = [0] * n

        for src, dest in edges:
            GRAPH[dest].append(src)

        def bfs(node):
            level = [node]
            seen = 1 << node
            org = node

            while level:
                next_level = []

                for node in level:
                    for adj in GRAPH[node]:
                        if not seen & (1 << adj):
                            answer[org] |= 1 << adj
                            seen |= 1 << adj

                            if answer[adj]:
                                answer[org] |= answer[adj]

                            else:
                                next_level.append(adj)

                level = next_level

        for node in range(n):
            bfs(node)

        return [[i for i in range(n) if (1 << i) & curr] for curr in answer]
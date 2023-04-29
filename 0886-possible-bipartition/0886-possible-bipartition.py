class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        GRAPH, COLORS = defaultdict(list), defaultdict(int)
        for node, adj in dislikes:
            GRAPH[node].append(adj)
            GRAPH[adj].append(node)
            
        for node in range(1, n+1):
            
            if node not in COLORS:
                COLORS[node] = 0
                queue = deque([node])

                while queue:
                    curr_node = queue.popleft()

                    for adj in GRAPH[curr_node]:
                        if adj not in COLORS:
                            COLORS[adj] = 1 - COLORS[curr_node]
                            queue.append(adj)

                        elif COLORS[adj] == COLORS[curr_node]:
                            return False

        return True
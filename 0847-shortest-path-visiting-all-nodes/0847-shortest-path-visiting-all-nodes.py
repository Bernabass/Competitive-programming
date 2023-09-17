class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        seen, queue = defaultdict(set), deque()

        for node in range(N):
            seen[node].add(node)
            queue.append((node, 0, {node}))

        while queue:
            curr_node, curr_cost, curr_seen = queue.popleft()

            if len(curr_seen) == N:
                return curr_cost

            for adj in graph[curr_node]:
                next_seen = curr_seen.copy()
                next_seen.add(adj)

                if tuple(next_seen) not in seen[adj]:
                    queue.append((adj, curr_cost + 1, next_seen))
                    seen[adj].add(tuple(next_seen))

        return -1
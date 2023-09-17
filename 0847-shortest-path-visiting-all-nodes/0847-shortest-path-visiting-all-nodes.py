class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        seen, queue = defaultdict(set), deque()

        for i in range(N):
            seen[i].add(tuple(sorted({i})))
            queue.append((i, 0, {i}))

        while queue:
            curr_node, curr_cost, curr_seen = queue.popleft()

            if len(curr_seen) == N:
                return curr_cost

            for adj in graph[curr_node]:
                next_seen = curr_seen.copy()
                next_seen.add(adj)

                if tuple(sorted(next_seen)) not in seen[adj]:
                    queue.append((adj, curr_cost + 1, next_seen))
                    seen[adj].add(tuple(sorted(next_seen)))

        return -1
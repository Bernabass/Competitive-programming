class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_GRAPH = defaultdict(list)
        group_INDEGREE = defaultdict(int)
        child_GRAPH = defaultdict(lambda: defaultdict(list))
        child_INDEGREE = defaultdict(int)

        for item, squad in enumerate(group):
            squad = squad if squad != -1 else 30001 + item
            group[item] = squad

            group_GRAPH[squad].extend([])
            child_GRAPH[squad][item].extend([])

            for prev in beforeItems[item]:
                if group[prev] != squad:
                    group[prev] = group[prev] if group[prev] != -1 else 30001 + prev
                    group_GRAPH[group[prev]].append(squad)
                    group_INDEGREE[squad] += 1
                else:
                    child_GRAPH[squad][prev].append(item)
                    child_INDEGREE[item] += 1

        def top_sort(graph, indegree):
            queue, order = deque(), []

            for node in graph.keys():
                if not indegree[node]:
                    queue.append(node)

            while queue:
                node = queue.popleft()
                order.append(node)

                for adj in graph[node]:
                    indegree[adj] -= 1

                    if not indegree[adj]:
                        queue.append(adj)

            return [] if len(order) != len(graph) else order

        group_acyclic = top_sort(group_GRAPH, group_INDEGREE)
        res = []

        if group_acyclic:
            for squad in group_acyclic:
                ans = top_sort(child_GRAPH[squad], child_INDEGREE)
                
                if not ans:
                    return
                
                res.extend(ans)

        return res
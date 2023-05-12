class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_GRAPH = {}
        group_INDEGREE = {}
        child_GRAPH = {}
        child_INDEGREE = {}

        for item, squad in enumerate(group):
            if squad == -1:
                group[item] = 30001 + item
                squad = 30001 + item

            group_GRAPH.setdefault(squad, [])
            child_GRAPH.setdefault(squad, {}).setdefault(item, [])

            for prev in beforeItems[item]:
                if group[prev] != squad:
                    if group[prev] == -1:
                        group[prev] = 30001 + prev

                    group_GRAPH.setdefault(group[prev], []).append(squad)
                    group_INDEGREE.setdefault(squad, 0)
                    group_INDEGREE[squad] += 1

                else:
                    child_GRAPH.setdefault(squad, {}).setdefault(prev, []).append(item)
                    child_INDEGREE.setdefault(item, 0)
                    child_INDEGREE[item] += 1

        def top_sort(graph, indegree):
            queue = []
            n = len(graph.keys())
            order = []

            for node in graph.keys():
                if not indegree.get(node, 0):
                    queue.append(node)

            while queue:
                node = queue.pop(0)
                order.append(node)

                for adj in graph.get(node, []):
                    if indegree.get(adj, 0):
                        indegree[adj] -= 1

                        if not indegree[adj]:
                            queue.append(adj)

            return [] if len(order) != n else order

        check = top_sort(group_GRAPH, group_INDEGREE)

        if check:
            for idx, val in enumerate(check):
                ans = top_sort(child_GRAPH.get(val, {}), child_INDEGREE)

                if not ans:
                    return []

                else:
                    check[idx] = ans

            return itertools.chain(*check)

        return []

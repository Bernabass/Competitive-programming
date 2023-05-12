class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_GRAPH, group_INDEGREE = defaultdict(list), defaultdict(int)
        child_GRAPH, child_INDEGREE = defaultdict(lambda: defaultdict(list)), defaultdict(int)
        for item, squad in enumerate(group):
            if squad == -1:
                group[item] = 30001 + item
                squad = 30001 + item
             
            group_GRAPH[squad].extend([])
            child_GRAPH[squad][item].extend([])
            for prev in beforeItems[item]:
                if group[prev] != squad:
                    if group[prev] == -1:
                        group[prev] = 30001 + prev
                    group_GRAPH[group[prev]].append(squad)
                    group_INDEGREE[squad] += 1
                
                else:
                    child_GRAPH[squad][prev].append(item)
                    child_INDEGREE[item] += 1
                    
    
        def top_sort(graph, indegree):
            queue, n = deque(), len(graph.keys())
            order = []
            
            for node in graph.keys():
                if not indegree[node]:
                    queue.append(node)
            
            while queue:
                node = queue.popleft()
                order.append(node)
                
                for adj in graph[node]:
                    if indegree[adj]:
                        indegree[adj] -= 1
                        
                        if not indegree[adj]:
                            queue.append(adj)
                            
                            
            return [] if len(order) != n else order
        
        check = top_sort(group_GRAPH, group_INDEGREE)

        if check:
            for idx, val in enumerate(check):
                ans = top_sort(child_GRAPH[val], child_INDEGREE)

                if not ans:
                    return []
                
                else:
                    check[idx] = ans
                   
            return itertools.chain(*check)
            
        return []
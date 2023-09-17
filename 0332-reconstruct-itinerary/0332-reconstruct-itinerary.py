class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        N = len(tickets)
        GRAPH = defaultdict(list)
        ans = ["JFK"]
        path = []
            
        for From, To in tickets:
            GRAPH[From].append(To)
            
        for key in GRAPH.keys():
            GRAPH[key].sort()
                        
        def dfs(node):
            if len(path) == N:
                ans.extend(path)
                return True

            for idx, adj in enumerate(GRAPH[node]):
                curr = GRAPH[node].pop(idx)
                path.append(adj)
                if dfs(adj):
                    return True
                
                GRAPH[node].insert(idx, curr)
                path.pop()
                
        dfs("JFK")

        return ans
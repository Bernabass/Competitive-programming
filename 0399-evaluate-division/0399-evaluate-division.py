class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
      
        GRAPH, ans = defaultdict(list), [-1]*(len(queries))
        for equation, value in zip(equations, values):
            a, b = equation
            GRAPH[a] += [(b, value)]
            GRAPH[b] += [(a, 1/value)]

        def bfs(a, b):
            queue, seen = deque([(a, 1)]), set()
            while queue:
                dividend, quotient = queue.popleft()
                if dividend == b:
                    return quotient
                seen.add(dividend)
                for divisor, value in GRAPH[dividend]:
                    if divisor not in seen: 
                        queue.append((divisor, quotient*value))

            return -1
        
        for idx, query in enumerate(queries):
            if query[0] in GRAPH and query[1] in GRAPH:
                ans[idx] = bfs(query[0], query[1])
                
        return ans
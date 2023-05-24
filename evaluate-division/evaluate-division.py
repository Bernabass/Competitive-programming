class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        GRAPH, ans = defaultdict(list), [-1]*len(queries)
        for idx, equation in enumerate(equations):
            A, B = equation
            GRAPH[A].append((B, values[idx]))
            GRAPH[B].append((A, 1 /values[idx]))
        
        def bfs(A, B):
            queue, seen = deque([(A, 1)]), set()
            while queue:
                dividend, quotient = queue.popleft()
                if dividend == B:
                    return quotient
                seen.add(dividend)
                for divisor, value in GRAPH[dividend]:
                    if divisor not in seen: 
                        queue.append((divisor, quotient*value))

            return -1
        
        for idx, query in enumerate(queries):
            C, D = query
            if C in GRAPH and D in GRAPH:
                ans[idx] = bfs(C, D)
                
        return ans
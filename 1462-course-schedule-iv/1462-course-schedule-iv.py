class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        GRAPH = defaultdict(list)
        ancestors = [set() for _ in range(numCourses)]
        res = [False]*len(queries)

        for src, dest in prerequisites:
            GRAPH[dest].append(src)

        def bfs(node):
            queue, seen = deque([node]), 1 << node

            while queue:
                curr = queue.popleft()

                for adj in GRAPH[curr]:
                    if not seen & (1 << adj):
                        ancestors[node].add(adj)
                        seen |= 1 << adj

                        if ancestors[adj]:
                            ancestors[node] |= ancestors[adj]

                        else:
                            queue.append(adj)

        for node in range(numCourses):
            bfs(node)
         
        for idx, val in enumerate(queries):
            for course1, course2 in [val]:
                if course1 in ancestors[course2]:
                    res[idx] = True
                    
        return res
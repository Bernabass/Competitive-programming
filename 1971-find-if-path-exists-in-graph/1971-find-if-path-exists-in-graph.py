class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        visited = {source}
        level = [source]
        while level:
            levelX = []
            for j in level:
                for k in graph[j]:
                    if k not in visited:
                        if k == destination:
                            return True
                        levelX.append(k)
                        visited.add(k)
            level = levelX
        return False
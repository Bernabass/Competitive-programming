class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        GRAPH = defaultdict(set)
        answer = [101]*n
        answer[0] = length = 0
        blue, red = set(map(tuple, blueEdges)), set(map(tuple, redEdges))
        seen = set()

        for parent, child in redEdges:
            GRAPH[parent].add(child)
 
        for parent, child in blueEdges:
            GRAPH[parent].add(child)
            
            
        level = [(0, 0, 1)]
        while level:
            length += 1
            next_level = []

            for parent in level:
                for color in parent[1:]:
                    for neighbour in GRAPH[parent[0]]:
                        edge = (parent[0], neighbour, 1-color)

                        if 1 - color:
                            if edge not in seen and edge[:2] in blue:
                                answer[neighbour] = min(length, answer[neighbour])
                                next_level.append((neighbour, 1))
                                seen.add((parent[0], neighbour, 1))

                        else:
                            if edge not in seen and edge[:2] in red:
                                answer[neighbour] = min(length, answer[neighbour])
                                next_level.append((neighbour, 0))
                                seen.add((parent[0], neighbour, 0))

            level = next_level
            
        answer = [-1 if i == 101 else i for i in answer]
        
        return answer
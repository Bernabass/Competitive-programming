from collections import defaultdict
n = int(input())
while n:
    GRAPH, COLOR = defaultdict(list), defaultdict(int)
    is_bicolorable = True
    
    for _ in range(int(input())):
        node, adj = map(int, input().split())
        GRAPH[node].append(adj)
        GRAPH[adj].append(node)
        
    level, COLOR[node] = [node], 0
    
    while level and is_bicolorable:
        next_level = []
        
        for node in level:
            for adj in GRAPH[node]:
                if adj not in COLOR:
                    COLOR[adj] = 1 - COLOR[node]
                    next_level.append(adj)
                    
                elif COLOR[node] == COLOR[adj]:
                    is_bicolorable = False
                         
        level = next_level
        
    if is_bicolorable:
        print("BICOLOURABLE.")
        
    else:
        print("NOT BICOLOURABLE.")
        
    n = int(input())
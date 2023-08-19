class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        def mst(ed, par, rank):
            
            def ins(n1):
                if n1 in par:
                    return
                par[n1] = n1
                rank[n1] = 1

            def find(n1):
                while n1 != par[n1]:
                    par[n1] = par[par[n1]]
                    n1 = par[n1]
                return n1

            def union(n1, n2):
                p1, p2 = find(n1), find(n2)
                if p1 == p2:
                    return 0
                if rank[p1] < rank[p2]:
                    p1, p2 = p2, p1
                par[p2] = p1
                rank[p1] += rank[p2]
                return 1

            e = sorted(ed, key = lambda x: x[2])
            res = 0
            
            for i, j, w in e:
                ins(i)
                ins(j)
                if union(i, j):
                    res += w
            
            return res if sum(i == find(i) for i in par) == 1 and len(par) == n else inf

        minWei = mst(edges, {}, {})
        critical = set()
        pseudo = set()
        
        for i in range(len(edges)):
            newEdges = edges[ : i] + edges[i + 1 : ]
            if mst(newEdges, {}, {}) > minWei:
                critical.add(i)
        
        for i in range(len(edges)):
            x, y, w = edges[i]
            if mst(edges, {x: x, y: x}, {x: 2, y: 1}) + w == minWei and i not in critical:
                pseudo.add(i)
        
        return [critical, pseudo]
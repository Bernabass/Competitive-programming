class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = list(range(n))
        
        def find(node):
            while node != parent[node]:
                node = parent[node]
                
            return node
        
        def union(a, b, m):
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            parent[pb] = pa
            
            for i, j in restrictions:
                if find(i) == find(j):
                    ans[m] = False
                    parent[pb] = pb
                    break
            
        
            
        ans = [True]*len(requests)

        for i in range(len(requests)):
            a, b = requests[i][0], requests[i][1]
            union(a, b, i)
            
        return ans
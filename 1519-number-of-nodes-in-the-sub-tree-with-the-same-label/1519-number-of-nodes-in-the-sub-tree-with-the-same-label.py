class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = defaultdict(list)
        for s,e in edges:
            tree[s].append(e)
            tree[e].append(s)
        
        res = [0] * n
        
        def dfs(node, par):
            nonlocal res
            count = Counter()
            for nei in tree[node]:
                if nei != par:
                    count += dfs(nei, node)
            
            count[labels[node]] += 1
            res[node] = count[labels[node]]
            
            return count
        
        dfs(0,-1)
        return res
        
        
        
        
        
        
        
#         graph = defaultdict(list)
#         ans = [0]*n
#         for i, j in edges:
#             parent, child = min(i,j), max(i,j)
#             graph[parent].append(child)
            
#         level = [0]
#         level_ordered = [level]
#         while level:
#             levelX = []
#             for i in level:
#                 for j in graph[i]:
#                     levelX.append(j)
#             level = levelX
#             if level:
#                 level_ordered.extend([level])
        
#         level_ordered.reverse()
        
#         print(level_ordered)
#         nth_level = defaultdict(lambda:1)
#         for level in level_ordered:
#             print(nth_level)
#             new_level = defaultdict(lambda:1)
#             for val in level:
#                 new_level[labels[val]] += nth_level[labels[val]]
#                 ans[val] = nth_level[labels[val]]
#             nth_level = new_level
         
#         return ans
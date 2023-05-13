from typing import List
from collections import defaultdict

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        GRAPH = defaultdict(list)
        time = [0]*n
        
        for adj, node in edges:
            GRAPH[node-1].append(adj-1)
            
        def dfs(node):
            if time[node]:
                return time[node]
             
            ans = 0 
            for adj in GRAPH[node]:
                ans = max(ans, dfs(adj))
                
            time[node] = ans + 1
            
            return time[node]
            
        for node in range(n):
            dfs(node)
            
        return " ".join(map(str, time))
            

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends

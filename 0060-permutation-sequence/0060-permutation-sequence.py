class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = [0]
        made = []
        def dfs(arr):
            if not arr:
                if ans[0] + 1 == k:
                    ans[0] = "".join(map(str, made))
                    return True
                
                ans[0] += 1
                    
                return False
            
            for i, num in enumerate(arr):
                made.append(num)
                res = dfs(arr[:i] + arr[i + 1:])
                if res:
                    return True
                
                made.pop()
                
        dfs(list(range(1, n + 1)))
        
        return ans.pop()  
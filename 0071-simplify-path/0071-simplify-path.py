class Solution:
    def simplifyPath(self, path: str) -> str:
        pathes = path.split('/')
        ans = []
        for val in pathes:
            if val == '..':
                if ans:
                    ans.pop()
                    
            elif val and val != '.':
                ans.append(val)
                
        return '/' + '/'.join(ans)
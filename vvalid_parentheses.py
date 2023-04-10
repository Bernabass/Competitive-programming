class Solution:
    def isValid(self, s: str) -> bool:
        base={'(':')','[':']','{':'}'}
        stack=[]
        for i in range(len(s)):
            if s[i] in base.keys():
                stack.append(s[i])
            else:
                if stack==[]:
                    return False
                if base[stack[-1]]!=s[i]:
                    return False
                else:
                    stack.pop()
        else:
            return stack==[]

    "new"

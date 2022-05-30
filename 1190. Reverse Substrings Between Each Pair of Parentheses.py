class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=['']
        for i in range(len(s)):
            if s[i]=='(':
                stack.append('')
            elif s[i]==')':
                temp=stack.pop()
                temp=list(temp)
                temp.reverse()
                temp=''.join(temp)
                stack[-1]+=temp
            else:
                stack[-1]+=s[i]
        return stack[0]
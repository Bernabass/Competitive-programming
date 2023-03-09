class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        tobe = []

        for i,c in enumerate(s):
            if c == '(': 
                if s[i-1] == '(':
                    tobe.append('(')

                if s[i-1] == ")":
                    tobe.append("+")


                if s[i+1] == "(":
                    tobe.append("2*")


                if s[i+1] == ")":
                    tobe.append("1")


            elif c == ")":
                if s[i-1] == c:
                    tobe.append(")")


        return eval("".join(tobe))
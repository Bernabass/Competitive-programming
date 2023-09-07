class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        ans, operators = [], ["+", "-", "*"]

        def back_track(idx, collected):
            for i in range(idx + 1, N + 1):
                if num[idx] == '0' and i > idx + 1:
                    continue
                curnum = num[idx:i]
                collected.append(curnum)
                if i == N:
                    expr = ''.join(collected)
                    if eval(expr) == target:
                        ans.append(expr)
                        
                elif i < N:
                    for sign in operators:
                        collected.append(sign)
                        back_track(i, collected)
                        collected.pop()
                        
                collected.pop()

        back_track(0, [])
        
        return ans
    
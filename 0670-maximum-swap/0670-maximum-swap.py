class Solution:
    def maximumSwap(self, num: int) -> int:
        stack, ans = [], []
        num = list(str(num))
        
        for index,digit in enumerate(num):
            if stack:
                count = -1
                while count >= -(len(stack)):
                    if digit < num[stack[count]]:
                        break
                    elif digit == num[stack[count]]:
                        count -= 1
                        continue
                        
                    pos_ans = [stack[count],index]
                    if ans:
                        if pos_ans[0] < ans[0]:
                            ans = pos_ans.copy()
                        elif pos_ans[0] == ans[0]:
                            if pos_ans[1] > ans[1]:
                                ans = pos_ans.copy()
                                
                    else:
                        ans = pos_ans.copy()
                    count -= 1
                
            stack.append(index)
          
        if ans:
            num[ans[0]], num[ans[1]] = num[ans[1]],num[ans[0]]
    
        return int("".join(num))
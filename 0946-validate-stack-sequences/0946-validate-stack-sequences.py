class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = j = 0
        stack=['', pushed[0]]
        
        while i < len(pushed) and j < len(popped):
            if stack[-1] != popped[j]:
                i += 1
                if i >= len(pushed):
                    break
                else:
                    stack.append(pushed[i])
            else:
                j += 1
                stack.pop()
                
        return stack == ['']
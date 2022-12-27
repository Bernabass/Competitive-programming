class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "#":
                right = stack.pop()
                left = stack.pop()
                res = chr(int(left + right) + 96)
                stack.append(str(res))
            else:
                stack.append(char)
        for idx in range(len(stack)):
            if stack[idx].isnumeric():
                stack[idx] = chr(int(stack[idx]) + 96)
                
        return "".join(stack)
                
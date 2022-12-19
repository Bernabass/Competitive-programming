class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = []
        operators = {'+','-','*','/'}
        for i in tokens:
            if i in operators:
                second = output.pop()
                first = output.pop()
                result = str(int((eval(first+i+second))))
                output.append(result)
            else:
                output.append(i)
        return int(output[0])  
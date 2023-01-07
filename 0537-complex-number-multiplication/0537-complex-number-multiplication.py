class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = list(map(int, num1.rstrip('i').split('+')))
        num2 =list(map(int, num2.rstrip('i').split('+')))
        real = num1[0] * num2[0] - num1[1] * num2[1]
        imag = num1[0] * num2[1] + num2[0] * num1[1]
        return f"{real}+{imag}i"
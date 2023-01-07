class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        num2 = num2.split("+")
        first = [int(num1[0]) * int(num2[0]),int(num1[0]) * int(num2[1][:-1])]
        second = [int(num1[1][:-1]) * int(num2[0]), -(int(num1[1][:-1]) * int(num2[1][:-1]))]
        second.reverse()
        res = [first[0] + second[0], first[1] + second[1]]
        return str(res[0]) + "+" + str(res[1]) + "i"
                  
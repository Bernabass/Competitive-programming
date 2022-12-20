class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 , n2 = len(num1) , len(num2)
        count1 , count2 = 0 , 0
        res1 , res2 = 0 , 0
        for i in range(n1-1,-1,-1):
            digit1 = 10**(i)
            temp = ord(num1[count1]) - 48
            res1 += temp * digit1
            count1 += 1
        for j in range(n2-1,-1,-1):
            digit2 = 10**(j)
            temp = ord(num2[count2]) - 48
            res2 += temp * digit2
            count2 += 1
        return str(res1 * res2)
    
        
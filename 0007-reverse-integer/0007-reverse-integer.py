class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        ans = int(str(abs(x))[::-1])
        if x < 0 :
            flag = True
            ans *= -1
        if ans < -1*((2**31)-1) or ans > (2**31)-1:
            return 0
        return ans
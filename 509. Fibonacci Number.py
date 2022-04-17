class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        if n>1:
            for i in range(n-1):
                c=a+b
                a,b=b,c
            return c
        else:
            return n
        
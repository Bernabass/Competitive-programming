class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        def isPowerOf4(n):
                if n==1:
                    return True
                else:
                    if n%4!=0:
                        return False
                    else:
                        return True and isPowerOf4((n/4))
        return isPowerOf4(n)

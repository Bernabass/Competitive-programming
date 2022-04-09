class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        def isPowerOfThre(n):
                if n==1:
                    return True
                else:
                    if n%3!=0:
                        return False
                    else:
                        return True and isPowerOfThre((n/3))
        return isPowerOfThre(n)

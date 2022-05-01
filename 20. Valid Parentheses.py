class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        keys={'(':1,'{':2,'[':3}
        values={')':-1,'}':-2,']':-3}
        out=[]
        for i in s:
            if i in keys:
                out.append(i)
            else:
                if out==[]:
                    return False
                else:
                    if keys[out[-1]]+values[i]==0:
                        out.pop()
                    else:
                        return False
        if out==[]:
            return True
        else:
            return False
class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(' ')
        output=[]
        for i in range(len(s)):
            for i in s:
                for j in s:
                    if i[-1]>j[-1]:
                        break
                else:
                    output.append(i[:-1])
                    s.remove(i)
        return ' '.join(output)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1,N2=len(text1),len(text2)
        dp={}
        def do(p1,p2):
            if p1==N1 or p2==N2:return 0
            elif (p1,p2) in dp:return dp[(p1,p2)]
            elif text1[p1]==text2[p2]:
                dp[(p1,p2)]=do(p1+1,p2+1)+1
                return dp[(p1,p2)]
            dp[(p1,p2)]=max(do(p1+1,p2),do(p1,p2+1))
            return dp[(p1,p2)]
        return do(0,0)
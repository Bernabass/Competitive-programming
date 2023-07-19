class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        @cache
        def back_track(idx1, idx2, idx3):
            one, two, three = s1[idx1:], s2[idx2:], s3[idx3:]
                     
            if one + two == three or two + one == three:
                return True
                        
        
            for i in range(idx1, n1):
                for j in range(idx2, n2):
                    if s1[idx1:i+1] + s2[idx2:j+1] == s3[idx3:i+j+2]:
                        if back_track(i+1, j+1, i+j+2):
                            return True
                        
                    else:
                        break
                        
            for i in range(idx2, n2):
                for j in range(idx1, n1):
                    if s2[idx2:i+1] + s1[idx1:j+1] == s3[idx3:i+j+2]:
                        if back_track(j+1, i+1, i+j+2):
                            return True
                        
                    else:
                        break
                        
                        
            return False
        
        return back_track(0, 0, 0)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 + n2 != len(s3):
            return False
        
        @cache
        def back_track(i, j):
            if i == n1 and j == n2:
                return 1
            
            choose_s1 = choose_s2 = 0
            
            if i < n1 and s1[i] == s3[i + j]:
                choose_s1 = back_track(i + 1, j)
                
            if j < n2 and s2[j] == s3[i + j]:
                choose_s2 = back_track(i, j + 1)

            return choose_s1 or choose_s2

        return back_track(0, 0)
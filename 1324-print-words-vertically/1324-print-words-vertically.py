class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        verticalized = []
        row_size, col_size = len(s), len(s[0])
        longest = 0
        for i in range(row_size):
            longest = max(longest,len(s[i]))
    
        for j in range(longest):
            nth_col = []
            for i in range(row_size):
                if j > len(s[i]) - 1:
                    nth_col.append(" ")
                    continue
                nth_col.append(s[i][j])
            verticalized.append(("".join(nth_col).rstrip()))
    
        return verticalized
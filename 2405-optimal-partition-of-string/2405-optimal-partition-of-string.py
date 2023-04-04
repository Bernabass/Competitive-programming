class Solution:
    def partitionString(self, s: str) -> int:
        ans = 0
        min_substring = set()

        for char in s:
            if char not in min_substring:
                min_substring.add(char)
                
            else:
                
                min_substring = set(char)
                ans += 1


        return ans + 1
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(list(s))
        for i in t:
            if i not in s or s[i] <= 0:
                return i
            else:
                s[i] -= 1
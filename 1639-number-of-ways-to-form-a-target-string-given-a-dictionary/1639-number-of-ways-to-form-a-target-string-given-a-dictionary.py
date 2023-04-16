class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, mod = len(target), 10**9 + 7
        res = [0] *(n+1)
        res[0] = 1
        for i in range(len(words[0])):
            count = Counter()
            for w in words:
                count[w[i]] += 1
            for j in range(n - 1, -1, -1):
                res[j + 1] += res[j] * count[target[j]] % mod
                
        return res[n] % mod


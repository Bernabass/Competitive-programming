class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = []
        hashed = Counter(deliciousness)
        count = 0
        for i in range(23):
            powers.append(2**i)
        for i in deliciousness:
            hashed[i] -= 1
            for j in powers:
                if (j - i) in hashed and hashed[j-i] > 0:
                    count += hashed[j-i]
            hashed[i] += 1
        return (count//2)%(10**9 + 7)
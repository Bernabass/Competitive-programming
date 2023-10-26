class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        info = defaultdict(int)
        ans, MOD = 0, 10**9 + 7
        
        for num in arr:
            count = 0
            for factor in info:
                if not num % factor and num // factor in info:
                    count += info[factor] * info[num // factor]
                    
            ans += count + 1
            info[num] = count + 1
            
        return ans % MOD
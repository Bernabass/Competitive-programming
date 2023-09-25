class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = list(zip(ages, scores))
        pairs.sort(reverse = True)
        N = len(scores)
        max_score = 0
        dp = [0] * N
        
        for idx, (age, score) in enumerate(pairs):
            dp[idx] = score
            for j in range(idx):
                if score <= pairs[j][1]:
                    dp[idx] = max(dp[idx], dp[j] + score)
                    
            max_score = max(max_score, dp[idx])
            
        return max_score

                    
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        memo = []
        for i in range(len(group) + 1):
            memo_i = []
            for j in range(minProfit + 1):
                memo_i.append([-1] * (n + 1))
            memo.append(memo_i)

        def count(crime_i: int, curr_prof: int, curr_mem: int) -> int:
            if curr_mem > n:
                return 0
            if crime_i >= len(group):
                return int(curr_prof >= minProfit and curr_mem <= n)
            
            if memo[crime_i][curr_prof][curr_mem] != -1:
                return memo[crime_i][curr_prof][curr_mem]
            
            not_pick = count(crime_i + 1, curr_prof, curr_mem)
            pick = count(crime_i + 1, min(minProfit, curr_prof + profit[crime_i]), curr_mem + group[crime_i])
            
            memo[crime_i][curr_prof][curr_mem] = (not_pick + pick) % (10 ** 9 + 7)
            
            return memo[crime_i][curr_prof][curr_mem]

        return count(0, 0, 0)



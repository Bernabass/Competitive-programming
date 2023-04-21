class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def count(crime_i, curr_prof, curr_mem):
            if curr_mem > n:
                return 0
            if crime_i >= len(group):
                return int(curr_prof >= minProfit and curr_mem <= n)
            
            
            not_pick = count(crime_i + 1, curr_prof, curr_mem)
            pick = count(crime_i+1, min(minProfit, curr_prof+profit[crime_i]), curr_mem+ group[crime_i])
                
            return  (not_pick + pick) % (10 ** 9 + 7)

        return count(0, 0, 0)
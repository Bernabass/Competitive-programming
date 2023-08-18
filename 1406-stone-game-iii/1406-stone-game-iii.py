class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [[0, 0] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            possible_ans = []
            if i < n:
                first_1, second_1 = dp[i + 1]
                first_ans_1, second_ans_1 = stoneValue[i] + second_1, first_1
                possible_ans.append((first_ans_1 - second_ans_1, (first_ans_1, second_ans_1)))
            if i + 1 < n:
                first_2, second_2 = dp[i + 2]
                first_ans_2, second_ans_2 = stoneValue[i] + stoneValue[i + 1] + second_2, first_2
                possible_ans.append((first_ans_2 - second_ans_2, (first_ans_2, second_ans_2)))
            if i + 2 < n:
                first_3, second_3 = dp[i + 3]
                first_ans_3, second_ans_3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + second_3, first_3
                possible_ans.append((first_ans_3 - second_ans_3, (first_ans_3, second_ans_3)))

            possible_ans.sort()
            dp[i] = possible_ans[-1][1]

        alice, bob = dp[0]

        if bob > alice:
            return "Bob"
        elif bob < alice:
            return "Alice"
        return "Tie"
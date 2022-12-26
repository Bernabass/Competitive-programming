class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = defaultdict(int)
        result = []
        for i in matches:
            players[i[0]] += 0
            players[i[1]] -= 1
        not_lost = []
        one_lost = []
        for outcome in players:
            if players[outcome] == 0:
                not_lost.append(outcome)
            if players[outcome] == -1:
                one_lost.append(outcome)
        not_lost.sort()
        one_lost.sort()
        result =[not_lost,one_lost]
        return result
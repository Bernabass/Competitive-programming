class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(parents)):
            graph[parents[i]].append(i)
        values = {}
        def dfs(node):
            if not graph[node]:
                values[node] = 1
                return 1
            temp = 1
            for neighbour in graph[node]:
                temp += dfs(neighbour)
            values[node] = temp
            return values[node]
        total = dfs(graph[-1][0])
        maximum = -float('inf')
        res = 1
        for j in values:
            if graph[j]:
                score = 1
                summ = 0
                for k in graph[j]:
                    summ += values[k]
                    score *= values[k]
                if total - (summ + 1):
                    score *= total - (summ + 1)
            else:
                score = total - 1
            if score > maximum:
                res = 1
                maximum = score
            elif score == maximum:
                res += 1
        return res
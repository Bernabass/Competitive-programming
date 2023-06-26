class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left, right = [(inf, -1)], [(inf, -1)]
        middle = deque()
        
        for idx, cost in enumerate(costs):
            if idx < candidates: 
                heappush(left, (cost, idx))
            elif idx >= len(costs) - candidates:
                heappush(right, (cost, idx))
            else:
                middle.append((cost, idx))


        total_cost = 0
        for _ in range(k):
            if left[0][0] <= right[0][0]:
                total_cost += heappop(left)[0]
                middle and heappush(left, middle.popleft())
            else:
                total_cost += heappop(right)[0]
                middle and heappush(right, middle.pop())

        return total_cost
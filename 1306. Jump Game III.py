class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = set([start])
        while queue:
            p = queue.popleft()
            if arr[p] == 0:
                return True
            if 0 <= p - arr[p]:
                neighb1 = p - arr[p]
                if neighb1 not in visited:
                    queue.appendleft(neighb1)
                    visited.add(neighb1)
            if p + arr[p] < len(arr):
                neighb2 = p + arr[p]
                if neighb2 not in visited:
                    queue.appendleft(neighb2)
                    visited.add(neighb2)
        return False
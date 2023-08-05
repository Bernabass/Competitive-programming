class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        n = len(positions)
        idx = sorted(range(n) , key=positions.__getitem__)
        stack = []

        for i in idx:
            while stack and directions[stack[-1]] == 'R' and directions[i] == 'L' and healths[i] != 0:
                diff = healths[stack[-1]] - healths[i]

                if diff == 0:
                    healths[i] = 0
                    healths[stack[-1]] = 0
                    stack.pop()
                if diff < 0:
                    healths[stack[-1]] = 0
                    healths[i] -= 1
                    stack.pop()
                if diff > 0:
                    healths[stack[-1]] -= 1
                    healths[i] = 0
            
            if healths[i]:
                stack.append(i)

        ans = []
        for val in healths:
            if val :
                ans.append(val)

        return  ans
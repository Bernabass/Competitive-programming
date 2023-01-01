class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n1 , n2 = len(s), len(spaces)
        s = deque(s)
        idx = ptr = 0
    
        while idx < n1:
            if ptr < n2 and idx == spaces[ptr]:
                temp = s.popleft()
                s.append(" ")
                s.append(temp)
                ptr += 1
            else:
                temp = s.popleft()
                s.append(temp)
    
            idx += 1 
    
        s = "".join(s)
        return s
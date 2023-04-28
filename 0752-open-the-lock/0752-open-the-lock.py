class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        seen = {"0000"}
        
        if target in seen:
            return 0
        
        if "0000" in deadends:
            return -1
        
        operations = [[0]*i + [j] + [0]*(3-i) for i in range(4) for j in [1, -1]]
        
        def add(arr1, arr2):
            ans = tuple((a+b) % 10 for a, b in zip(arr1, arr2))
            
            return "".join(map(str, ans)), ans

        level = [(0, 0, 0, 0)]
        turns = 0
        while level:
            turns += 1
            next_level = []
            
            for state in level:
                for oper in operations:
                    code = add(state, oper)
                    
                    if code[0] == target:
                        return turns
                    
                    if code[0] not in deadends and code[0] not in seen:
                        next_level.append(code[1])
                        seen.add(code[0])
                        
            level = next_level
                     
        return -1
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = list(map(ord, list(s)))
        added = [0]*n
        
        for query in shifts:
            left, right = query[0], query[1]
            forward = query[2]
            
            if forward:
                if 0 <= left < n:
                    added[left] += 1
                    
                if right + 1 < n:
                    added[right+1] -= 1
                    
            else:
                if 0 <= left < n:
                    added[left] += -1

                if right + 1 < n:
                    added[right+1] -= -1
            
            
        for i in range(1, len(added)):
            added[i] += added[i-1]
            
            
        for idx, order in enumerate(arr):
            order += added[idx]  
            arr[idx] = chr((order - 97 ) % 26 + 97)
            
        return "".join(arr)
                    
                  
                    
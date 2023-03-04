class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = list(map(ord, list(s)))
        added = [0]*(n+1)
        
        for query in shifts:
            left, right = query[0], query[1]
            forward = query[2]
            
            if forward:
                added[left] += 1  
                added[right+1] -= 1
                    
            else:
                added[left] += -1
                added[right+1] -= -1
            
            
        for i in range(1, len(added)):
            added[i] += added[i-1]
            
            
        for idx, order in enumerate(arr):
            order += added[idx]  
            arr[idx] = chr((order - 97 ) % 26 + 97)
            
        return "".join(arr)  
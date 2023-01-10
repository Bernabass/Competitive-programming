class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        org = len(code)
        if not k:
            return [0]*org
        elif k < 0:
            initial = org + k
        else:
            initial = 1
            
        code.extend(code)
        n = len(code)
        window_size = abs(k)
        prev = sum(code[initial:initial+window_size])
        decrypted_code = [prev]
        start = initial+window_size
    
        for idx in range(start,org+start-1):
            curr = prev - code[idx-window_size] + code[idx]
            decrypted_code.append(curr)
            prev = curr
            
        return decrypted_code
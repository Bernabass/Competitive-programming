class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        org = len(code)
        if not k:
            return [0]*len(code)
        elif k < 0:
            initial = len(code) + k
        else:
            initial = 1
            
        code.extend(code)
        n = len(code)
        window_size = abs(k)
        prev = sum(code[initial:initial+window_size])
        decrypted_code = [prev]

        for idx in range(initial+window_size,org+initial+window_size-1):
            curr = prev - code[idx-window_size] + code[idx]
            decrypted_code.append(curr)
            prev = curr
            
        return decrypted_code
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        present = ""
        
        for char in order:
            if char in freq:
                present += freq[char] * char
                del freq[char]
                    
        for char, val in freq.items():
            present += val * char
                
        return present
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        result = ""
        
        for char in order:
            if char in freq:
                result += freq[char] * char
                del freq[char]
                    
        for char, val in freq.items():
            result += val * char
                
        return result
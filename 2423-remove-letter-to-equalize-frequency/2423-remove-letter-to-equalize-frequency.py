class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        freq2 = Counter(freq.values())
        
        if len(freq2) <= 2:
            max_key, min_key = max(freq2.keys()), min(freq2.keys())
            
            if len(freq2) == 1 and (min_key == 1 or freq2[min_key] == 1):
                return True
            
            elif (max_key - min_key == 1 and freq2[max_key] == 1) or (min_key == 1 and freq2[min_key] == 1):
                return True
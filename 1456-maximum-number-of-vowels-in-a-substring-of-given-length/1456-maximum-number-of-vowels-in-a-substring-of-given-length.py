class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowles = {"a","e","i","o","u"}
        curr_vowles = max_vowles = 0
        
        for i in range(k):
            if s[i] in vowles:
                curr_vowles += 1
                
        max_vowles = curr_vowles
                
                
        for j in range(k,len(s)):
            if s[j] in vowles:
                curr_vowles += 1
                
            if s[j-k] in vowles:
                curr_vowles -= 1
                
            max_vowles = max(max_vowles, curr_vowles)
            
            
        return max_vowles
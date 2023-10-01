class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = s.split()
        arr = [word[::-1] for word in sentence]
        
        return " ".join(arr)
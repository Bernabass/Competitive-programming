class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        info = set(dictionary)
        arr = sentence.split()
        
        for idx, word in enumerate(arr):
            curr = ""
            
            for char in word:
                curr += char
                
                if curr in info:
                    arr[idx] = curr
                    break
                    
        return " ".join(arr)
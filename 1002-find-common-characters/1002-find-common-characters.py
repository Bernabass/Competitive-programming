class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        check = words[0]
        n = len(words)
        elements, ans = [], []
        
        for i in range(1,n):
            elements.append(Counter(words[i]))
        
        for char in check:
            for i in elements:
                if char in i and i[char] > 0:
                    i[char] -= 1
                    continue
                break
            else:
                ans.append(char)
                
        return ans 
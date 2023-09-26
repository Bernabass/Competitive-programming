class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = Counter(s)
        stack, prev = [], set()
        
        for char in s:
            if char not in prev:
                while stack and char < stack[-1] and freq[stack[-1]] - 1 > 0:
                    prev.remove(stack[-1])
                    freq[stack[-1]] -= 1
                    stack.pop()
             
                stack.append(char)
                prev.add(char)
                
            else:
                freq[char] -= 1
            
        return "".join(stack)
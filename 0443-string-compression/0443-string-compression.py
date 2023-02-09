class Solution:
    def compress(self, chars: List[str]) -> int:
        s = f"{chars[0]}"
        count = 1
        
        for i in range(1, len(chars)):
            if chars[i] == s[-1]:
                count += 1
                continue

            if count > 1:
                s = s + str(count) + chars[i]
                count = 1
            else:
                s += chars[i]
                
        if count > 1:
            s += str(count)
        
        for i in range(len(s)):
            chars[i] = s[i]
            
        for _ in range(len(chars) - len(s)):
            chars.pop()
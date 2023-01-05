class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        left = right = size = goods = 0
        prev = set()
        
        while right < n:
            if s[right] not in prev:
                prev.add(s[right])
                size += 1
            else:
                if s[left] == s[right]:
                    left += 1
                    right = left
                else:
                    left = right
                size = 1
                prev = set(s[right])
            if size == 3:
                goods += 1
                prev.remove(s[left])
                left += 1
                size -= 1
            right += 1
        
        return goods
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        check = set()
        res = 0
        count = 0
        while right < len(s) and left < len(s):
            if s[right] not in check:
                check.add(s[right])
                right += 1
                count += 1
            else:
                check.remove(s[left])
                left += 1
                count -= 1
            res = max(res,count)
        return res
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(filter(str.isalnum,s))
        s=s.lower()
        temp=s[::-1]
        return s==temp
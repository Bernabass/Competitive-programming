class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0 or (x and not (x % 10)):
            return False

        first_half = 0
        while x > first_half:
            first_half = first_half * 10 + (x % 10)
            x //= 10

        return first_half == x or  (first_half // 10) == x
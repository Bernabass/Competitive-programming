class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        @cache
        def rec(n):
            if n <= 26:
                return chr(n + 64)
            
            quotient, remainder = divmod(n, 26)
            if not remainder:
                return rec(quotient - 1) + "Z"
            
            return rec(quotient) + chr(remainder + 64)

        return rec(columnNumber)
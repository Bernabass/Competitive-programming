class Solution:
    def isNumber(self, s: str) -> bool:
        def IsDecimal(s):
            if not s:
                return False
            if s[0] in {"-", "+"}:
                if len(s) == 1:
                    return False

                s = s[1:].split(".")

            else:
                s = s.split(".")

            if "-" in s[1:] or "+" in s[1:]:
                return False

            if len(s) > 2:
                return False

            if len(s) == 1:
                return s[0].isdigit()

            if s[0] == s[1] == "":
                return False

            if s[0] and not s[0].isdigit():
                return False

            if s[1] and not s[1].isdigit():
                return False

            return True

        def IsInteger(s):
            if not s:
                return False
            if s[0] in {"-", "+"}:
                if len(s) == 1:
                    return False

                s = s[1:]

            return s.isdigit()
        
        s = re.split('[eE]', s)
        
        if len(s) > 2:
            return False
        
        if len(s) == 1:
            return IsDecimal(s[0]) or IsInteger(s[0])
        
        return (IsDecimal(s[0]) or IsInteger(s[0])) and (IsInteger(s[1])) 
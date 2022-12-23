class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        count = 0
        while count < len(command):
            if command[count] == "G":
                res += "G"
                count += 1
            elif command[count] == "a":
                res += "al"
                count += 3
            elif command[count] == ")":
                res += "o"
                count += 1
            else:
                count += 1
        return res
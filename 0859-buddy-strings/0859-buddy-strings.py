class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) < len(s)

        diff = []
        for a, b in zip(s, goal):
            if a != b:
                diff.append((a, b))

        if len(diff) != 2:
            return False

        return diff[0] == diff[1][::-1]
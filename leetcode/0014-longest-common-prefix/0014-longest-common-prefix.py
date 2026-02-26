class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        N = len(strs)

        def match(prev, curr):
            longest_match = []

            for i in range(min(len(prev), len(curr))):
                if prev[i] != curr[i]:
                    return longest_match

                longest_match.append(curr[i])

            return longest_match

        for i in range(1, N):
            res = match(res, strs[i])

        return "".join(res)
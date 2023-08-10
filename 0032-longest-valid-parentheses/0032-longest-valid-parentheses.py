class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = idx = 0
        reference, n = -1, len(s)
        stack = []

        while idx < n:
            curr_bracket = s[idx]
            curr_ans = 0

            if curr_bracket == ")":
                if stack:
                    stack.pop()
                    if stack:
                        curr_ans = idx - stack[-1]

                    else:
                        curr_ans = idx - reference

                else:
                    reference = idx

            else:
                stack.append(idx)

            idx += 1
            ans = max(ans, curr_ans)

        return ans
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        diff_counter = Counter()
        nice_pairs = 0

        def rev(num):
            return int(str(num)[::-1])

        for num in nums:
            curr_diff = num - rev(num)
            nice_pairs += diff_counter[curr_diff]
            diff_counter[curr_diff] += 1

        return nice_pairs % (10 ** 9 + 7)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def back_track(idx, target):
            if (idx, target) in memo:
                return memo[(idx, target)]

            if target < 0:
                return 0

            if target == 0:
                return 1

            count = 0

            if idx < len(coins):
                count += back_track(idx, target-coins[idx])
                count += back_track(idx+1, target)
            memo[(idx, target)] = count

            return count

        return back_track(0, amount)

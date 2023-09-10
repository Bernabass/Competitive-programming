class Solution:
    def countOrders(self, n: int) -> int:
        
        @cache
        def dp(pickups, deliveries):
            if pickups == deliveries == 0:
                return 1

            count1 = count2 = 0

            if pickups:
                count1 = pickups * dp(pickups - 1, deliveries + 1)
            
            if deliveries:
                count2 = deliveries * dp(pickups, deliveries - 1)

            return count1 + count2

        return dp(n, 0) % (10**9 + 7)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], dp[a - c] + 1)
        return dp[n] if dp[n] != float("inf") else -1

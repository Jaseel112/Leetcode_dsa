class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for x in coins:
                if i-x>=0:
                    dp[i] = min(dp[i-x]+1,dp[i])
        return dp[amount] if dp[amount]!=amount+1 else -1

            
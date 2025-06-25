class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for x in coins:
                if i-x>=0:
                    dp[i] = min(dp[i-x]+1,dp[i])
        return dp[amount] if dp[amount]!=amount+1 else -1


        # hashmap={}
        # result=[amount+1]
        # flag=[0]
        # if amount==0:
        #     return 0
        
        # def backtrack(amount,count):
        #     if amount==0:
        #         flag[0]=1
        #         result[0]=min(result[0],count)
        #         return 
        #     if amount<0:
        #         return 
        #     for i in range(len(coins)):
        #             count+=1
        #             backtrack(amount-coins[j],count)
        #             count-=1
        # backtrack(amount,0)
        # return result[0] if flag[0] else -1



            
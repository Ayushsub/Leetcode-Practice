from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]=minimum coins needed for amount i
        dp=[float('inf')]*(amount+1)
        #Base case
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                #If coin can be used
                if i-coin>=0:
                    dp[i]=min(dp[i],1+dp[i-coin])
        return dp[amount] if dp[amount]!=float('inf') else -1
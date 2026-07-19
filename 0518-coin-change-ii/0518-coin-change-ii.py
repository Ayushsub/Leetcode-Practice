class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[j]=ways to make sum j
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            # Forward since coins are unlimited
            for j in range(coin,amount+1):
                dp[j]+=dp[j-coin]
        return dp[amount]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         n=len(coins)
#         # dp[i][j]=ways using first i coins
#         dp=[[0]*(amount+1) for _ in range(n+1)]
#         for i in range(n+1):
#             dp[i][0]=1
#         for i in range(1,n+1):
#             for j in range(amount+1):
#                 # Skip coin
#                 dp[i][j]=dp[i-1][j]
#                 # Take coin
#                 if coins[i-1]<=j:
#                     dp[i][j]+=dp[i][j-coins[i-1]]
#         return dp[n][amount]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         memo={}
#         # memo[(i,rem)]=ways
#         def dfs(i,rem):
#             if rem==0:
#                 return 1
#             if rem<0 or i==len(coins):
#                 return 0
#             if (i,rem) in memo:
#                 return memo[(i,rem)]
#             take=dfs(i,rem-coins[i])
#             skip=dfs(i+1,rem)
#             memo[(i,rem)]=take+skip
#             return memo[(i,rem)]
#         return dfs(0,amount)


# def allWays(amount,coins):
#     ans=[]
#     def dfs(i,rem,path):
#         if rem==0:
#             ans.append(path[:])
#             return
#         if rem<0 or i==len(coins):
#             return
#         # Take coin
#         path.append(coins[i])
#         dfs(i,rem-coins[i],path)
#         path.pop()
#         # Skip coin
#         dfs(i+1,rem,path)
#     dfs(0,amount,[])
#     return ans
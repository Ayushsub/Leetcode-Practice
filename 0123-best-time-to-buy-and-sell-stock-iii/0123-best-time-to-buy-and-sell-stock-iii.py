class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1]*3 for _ in range(2)] for _ in range(n)]
        def dfs(i,buy,cap):
            if i==n or cap==0:
                return 0
            if dp[i][buy][cap]!=-1:
                return dp[i][buy][cap]
            if buy:
                dp[i][buy][cap]=max(
                    -prices[i]+dfs(i+1,0,cap),
                    dfs(i+1,1,cap)
                )
            else:
                dp[i][buy][cap]=max(
                    prices[i]+dfs(i+1,1,cap-1),
                    dfs(i+1,0,cap)
                )
            return dp[i][buy][cap]

        return dfs(0,1,2)
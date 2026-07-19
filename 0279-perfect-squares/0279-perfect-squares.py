class Solution:
    def numSquares(self, n: int) -> int:
        squares=[i*i for i in range(1,int(n**0.5)+1)]
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for square in squares:
            for j in range(square,n+1):
                dp[j]=min(dp[j],1+dp[j-square])
        return dp[n]
        
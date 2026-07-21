class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
        return dp[m-1][n-1]  


# class Solution:
#     def minPathSum(self,grid):
#         m=len(grid)
#         n=len(grid[0])
#         dp=[[-1]*n for _ in range(m)]
#         def dfs(i,j):
#             if i>=m or j>=n:
#                 return float("inf")
#             if i==m-1 and j==n-1:
#                 return grid[i][j]
#             if dp[i][j]!=-1:
#                 return dp[i][j]
#             dp[i][j]=grid[i][j]+min(dfs(i+1,j),dfs(i,j+1))
#             return dp[i][j]
#         return dfs(0,0)
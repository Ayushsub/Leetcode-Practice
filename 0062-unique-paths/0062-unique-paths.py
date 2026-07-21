class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

# from math import comb
# class Solution:
#     def uniquePaths(self,m:int,n:int)->int:
#         return comb(m+n-2,m-1)



# class Solution:
#     def uniquePaths(self,m:int,n:int)->int:
#         memo={}
#         def dfs(i,j):
#             if i==m-1 and j==n-1:
#                 return 1
#             if i>=m or j>=n:
#                 return 0
#             if (i,j) in memo:
#                 return memo[(i,j)]
#             memo[(i,j)]=dfs(i+1,j)+dfs(i,j+1)
#             return memo[(i,j)]
#         return dfs(0,0)
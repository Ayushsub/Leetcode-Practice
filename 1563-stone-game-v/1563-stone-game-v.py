class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n=len(stoneValue)
        dp=[[0]*n for _ in range(n)]
        mx=[[0]*n for _ in range(n)]
        for i in range(n):
            mx[i][i]=stoneValue[i]
        for j in range(1,n):
            mid=j
            sm=stoneValue[j]
            right=0
            for i in range(j-1,-1,-1):
                sm+=stoneValue[i]
                while (right+stoneValue[mid])*2<=sm:
                    right+=stoneValue[mid]
                    mid-=1
                if right*2==sm:
                    dp[i][j]=mx[i][mid]
                if mid!=i:
                    dp[i][j]=max(dp[i][j],mx[i][mid-1])
                if mid!=j:
                    dp[i][j]=max(dp[i][j],mx[j][mid+1])
                mx[i][j]=max(mx[i][j-1],dp[i][j]+sm)
                mx[j][i]=max(mx[j][i+1],dp[i][j]+sm)
        return dp[0][n-1]
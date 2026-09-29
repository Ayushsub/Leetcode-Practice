class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m,n=len(grid),len(grid[0])
        if grid[0][0]==')' or grid[m-1][n-1]=='(':
            return False
        if (m+n)%2==0:
            return False
        dp=[[set() for _ in range(n)] for _ in range(m)]
        dp[0][0]={1}
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                x=1 if grid[i][j]=='(' else -1
                if i>0:
                    for b in dp[i-1][j]:
                        if b+x>=0:
                            dp[i][j].add(b+x)
                if j>0:
                    for b in dp[i][j-1]:
                        if b+x>=0:
                            dp[i][j].add(b+x)
        return 0 in dp[m-1][n-1]
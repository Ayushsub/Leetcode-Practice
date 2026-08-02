class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        dp=[[None]*n for _ in range(n)]
        def dfs(l,r):
            if l==r:
                return piles[l]
            if dp[l][r]!=None:
                return dp[l][r]
            left=piles[l]-dfs(l+1,r)
            right=piles[r]-dfs(l,r-1)
            dp[l][r]=max(left,right)
            return dp[l][r]
        return dfs(0,n-1)>=0
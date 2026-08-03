class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        dp=[None]*(n+1)
        def dfs(i):
            if i>=n:
                return 0
            if dp[i]!=None:
                return dp[i]
            ans=float("-inf")
            curr=0
            for k in range(3):
                if i+k<n:
                    curr+=stoneValue[i+k]
                    ans=max(ans,curr-dfs(i+k+1))
            dp[i]=ans
            return ans
        diff=dfs(0)
        if diff>0:
            return "Alice"
        elif diff<0:
            return "Bob"
        return "Tie"

#dfs(i)=maximum score difference (current player-opponent) starting from index i
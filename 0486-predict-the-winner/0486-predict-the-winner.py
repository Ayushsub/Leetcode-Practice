class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[[None]*n for _ in range(n)]
        def dfs(l,r):
            if l==r:
                return nums[l]
            if dp[l][r]!=None:
                return dp[l][r]
            left=nums[l]-dfs(l+1,r)
            right=nums[r]-dfs(l,r-1)
            dp[l][r]=max(left,right)
            return dp[l][r]
        return dfs(0,n-1)>=0
#dfs(l,r)=maximum difference (current player score-opponent score) from subarray nums[l:r+1]

# class Solution:
#     def predictTheWinner(self,nums:List[int])->bool:
#         n=len(nums)
#         dp=[[0]*n for _ in range(n)]
#         for i in range(n):
#             dp[i][i]=nums[i]
#         for length in range(2,n+1):
#             for l in range(n-length+1):
#                 r=l+length-1
#                 dp[l][r]=max(nums[l]-dp[l+1][r],nums[r]-dp[l][r-1])
#         return dp[0][n-1]>=0  
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         s=sum(nums)
#         if abs(target)>s or (s+target)%2:
#             return 0
#         t=(s+target)//2
#         dp=[0]*(t+1)
#         dp[0]=1
#         for num in nums:
#             for j in range(t,num-1,-1):
#                 dp[j]+=dp[j-num]
#         return dp[t]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        # memo[(i,s)]=ways from index i with sum s
        def dfs(i,s):
            # All numbers used
            if i==len(nums):
                return 1 if s==target else 0
            if (i,s) in memo:
                return memo[(i,s)]
            # Try + and -
            memo[(i,s)]=dfs(i+1,s+nums[i])+dfs(i+1,s-nums[i])
            return memo[(i,s)]
        return dfs(0,0)

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         # Try + and - for every number
#         def dfs(i,s):
#             # All numbers used
#             if i==len(nums):
#                 return 1 if s==target else 0
#             return dfs(i+1,s+nums[i])+dfs(i+1,s-nums[i])
#         return dfs(0,0)
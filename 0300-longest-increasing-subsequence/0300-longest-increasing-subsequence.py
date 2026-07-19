class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        #dp[i]=LIS ending at index i
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                #Increasing sequence
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         memo={}
#         #memo[(i,prev)]=LIS length from i
#         def dfs(i,prev):
#             if i==len(nums):
#                 return 0
#             if (i,prev) in memo:
#                 return memo[(i,prev)]
#             take=0
#             if prev==-1 or nums[i]>nums[prev]:
#                 take=1+dfs(i+1,i)
#             skip=dfs(i+1,prev)
#             memo[(i,prev)]=max(take,skip)
#             return memo[(i,prev)]
#         return dfs(0,-1)
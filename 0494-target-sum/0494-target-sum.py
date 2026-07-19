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


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         total = sum(nums)

#         # Impossible if target is outside possible sum range
#         if abs(target) > total:
#             return 0

#         # P = (target + total) / 2 must be an integer
#         if (target + total) % 2:
#             return 0

#         target_sum = (target + total) // 2

#         # dp[i] = number of ways to form sum i
#         dp = [0] * (target_sum + 1)
#         dp[0] = 1

#         # 0/1 Knapsack: count subsets with sum = target_sum
#         for num in nums:
#             # Traverse backwards so each number is used once
#             for s in range(target_sum, num - 1, -1):
#                 dp[s] += dp[s - num]

#         return dp[target_sum]
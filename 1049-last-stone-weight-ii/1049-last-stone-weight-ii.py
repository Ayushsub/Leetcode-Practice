class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        target=total//2
        # dp[s]=True if sum s is possible
        dp=[False]*(target+1)
        dp[0]=True
        for stone in stones:
            # Traverse backwards
            for s in range(target,stone-1,-1):
                dp[s]=dp[s] or dp[s-stone]
        for s in range(target,-1,-1):
            if dp[s]:
                return total-2*s


# class Solution:
#     def lastStoneWeightII(self, stones: List[int]) -> int:
#         total=sum(stones)
#         # Return max subset sum <= total//2
#         def dfs(i,cur):
#             if i==len(stones):
#                 return cur
#             take=0
#             if cur+stones[i]<=total//2:
#                 take=dfs(i+1,cur+stones[i])
#             notTake=dfs(i+1,cur)
#             return max(take,notTake)
#         best=dfs(0,0)
#         return total-2*best


# class Solution:
#     def lastStoneWeightII(self, stones: List[int]) -> int:
#         total=sum(stones)
#         memo={}
#         # memo[(i,cur)]=best subset sum
#         def dfs(i,cur):
#             if i==len(stones):
#                 return cur
#             if (i,cur) in memo:
#                 return memo[(i,cur)]
#             take=0
#             if cur+stones[i]<=total//2:
#                 take=dfs(i+1,cur+stones[i])
#             notTake=dfs(i+1,cur)
#             memo[(i,cur)]=max(take,notTake)
#             return memo[(i,cur)]
#         best=dfs(0,0)
#         return total-2*best
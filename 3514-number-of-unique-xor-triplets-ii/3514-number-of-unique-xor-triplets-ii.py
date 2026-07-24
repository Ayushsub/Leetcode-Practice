class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        m=2048
        dp=[0]*m
        dp[0]=1
        for _ in range(3):
            ndp=[0]*m
            for x in range(m):
                if dp[x]:
                    for v in nums:
                        ndp[x^v]=1
            dp=ndp
        return sum(dp)
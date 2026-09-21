class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans=[0]*k
        dp=[0]*k
        for num in nums:
            r=num%k
            ndp=[0]*k
            ndp[r]+=1
            for p in range(k):
                ndp[p*r%k]+=dp[p]
            dp=ndp
            for r in range(k):
                ans[r]+=dp[r]
        return ans
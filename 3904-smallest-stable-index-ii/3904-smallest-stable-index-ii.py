class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        suff=[0]*n
        suff[-1]=nums[-1]
        for i in range(n-2,-1,-1):
            suff[i]=min(nums[i],suff[i+1])
        mx=nums[0]
        for i in range(n):
            mx=max(mx,nums[i])
            if mx-suff[i]<=k:
                return i
        return -1
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        f={}
        l=0
        a=0
        for r in range(len(nums)):
            f[nums[r]]=f.get(nums[r],0)+1
            while f[nums[r]]>k:
                f[nums[l]]-=1
                l+=1
            a=max(a,r-l+1)
        return a
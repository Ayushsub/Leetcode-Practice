class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                p=max(p,((nums[i]-1)*(nums[j]-1)))
        return p

        
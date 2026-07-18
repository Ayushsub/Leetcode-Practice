class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total=sum(nums)
        curMax=maxSum=nums[0]
        curMin=minSum=nums[0]
        for x in nums[1:]:
            curMax=max(x,curMax+x)
            maxSum=max(maxSum,curMax)
            curMin=min(x,curMin+x)
            minSum=min(minSum,curMin)
        if maxSum<0:
            return maxSum
        return max(maxSum,total-minSum)
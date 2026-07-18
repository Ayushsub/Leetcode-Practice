class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0  #max money till previous house
        prev2 = 0  #max money till house before previous
        for num in nums:
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp
        return prev1
        
#dp[i]=max(dp[i−1], dp[i−2]+nums[i])
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x=0
        for n in nums:x^=n
        if x:return len(nums)
        return len(nums)-1 if any(nums) else 0
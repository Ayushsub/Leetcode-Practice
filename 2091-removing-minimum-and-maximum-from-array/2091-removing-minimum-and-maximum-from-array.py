class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        min_idx=nums.index(min(nums))
        max_idx=nums.index(max(nums))
        i=min(min_idx,max_idx)
        j=max(min_idx,max_idx)
        front=j+1
        back=n-i
        both=(i+1)+(n-j)

        return min(front,back,both)
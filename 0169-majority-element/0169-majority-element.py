class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mc=1
        max_c=nums[0]
        for i in range(1,len(nums)):
            if mc==0:
                max_c=nums[i]
                mc=1
            elif nums[i]!=max_c:
                mc-=1
            elif nums[i]==max_c:
                mc+=1
        return max_c

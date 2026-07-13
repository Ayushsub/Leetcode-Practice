class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c_max=0
        max_=0
        for i in nums:
            if i==0:
                c_max=0
            else:
                c_max+=1
            max_=max(max_,c_max)
        return max_
        
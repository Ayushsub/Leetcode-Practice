class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=min(nums)
        l=max(nums)
        a=[]
        for i in range(s,l+1):
            if i not in nums:
                a.append(i)
        a.sort()
        return a
        
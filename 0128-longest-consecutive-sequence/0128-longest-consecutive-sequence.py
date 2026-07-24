class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for x in s:
            if x-1 not in s:
                l=1
                while x+l in s:
                    l+=1
                longest=max(longest,l)
        return longest


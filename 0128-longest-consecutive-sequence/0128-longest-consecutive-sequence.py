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

#So O(n × n)=O(n²). This reasoning would be correct only if the while ran n times for every iteration of the for loop. It doesn't. it is O(n)
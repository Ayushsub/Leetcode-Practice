class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        l=len(nums)
        if l<3:
            return l
        return 1<<l.bit_length()
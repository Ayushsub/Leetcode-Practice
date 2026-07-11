class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
        
        

"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
"""
        
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)

        for i in range(len(nums)):
            ans ^= i
            ans ^= nums[i]

        return ans

        (0 ^ 0) ^ (1 ^ 1) ^ (3 ^ 3) ^ 2
"""
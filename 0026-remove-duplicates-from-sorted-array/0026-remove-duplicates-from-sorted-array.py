class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = sorted(set(nums))
        for i in range(len(x)):
            nums[i] = x[i]
        return len(x)
        
"""
The problem asks  to modify the array in-place without using extra space.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k


"""
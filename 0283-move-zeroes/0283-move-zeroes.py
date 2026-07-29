class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[last_non_zero],nums[i]=nums[i],nums[last_non_zero]
                last_non_zero+=1

        """
        Do not return anything, modify nums in-place instead.
        """

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         i, j = 0, 0
#         n = len(nums)

#         while True:
#             while i < n and nums[i] != 0:
#                 i += 1

#             while j < n and nums[j] == 0:
#                 j += 1

#             if i >= n or j >= n:
#                 break

#             if i < j:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#                 j += 1
#             else:
#                 j += 1
        
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set(nums1)
        a=[]
        for i in range(len(nums2)):
            if nums2[i] in s:
                a.append(nums2[i])
                s.remove(nums2[i])
        return a


        
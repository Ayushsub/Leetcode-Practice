class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1=set(nums1)
        a0=set()
        for x in nums2:
            if x not in n1:
                a0.add(x)
        ans=[]
        n2=set(nums2)
        a1=set()
        for x in nums1:
            if x not in n2:
                a1.add(x)

        ans.append(list(a1))
        ans.append(list(a0))
        return ans
# from math import gcd
# class Solution:
#     def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
#         gp=[]
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 gp.append(gcd(nums[i],nums[j]))

#         gp.sort()
#         ans=[]
#         for  i in range(len(queries)):
#             ans.append(gp[queries[i]])
#         return ans     
from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx=max(nums)
        freq=[0]*(mx+1)
        for x in nums:
            freq[x]+=1

        cnt=[0]*(mx+1)
        for d in range(1,mx+1):
            for m in range(d,mx+1,d):
                cnt[d]+=freq[m]

        exact=[0]*(mx+1)
        for g in range(mx,0,-1):
            exact[g]=cnt[g]*(cnt[g]-1)//2
            for m in range(2*g,mx+1,g):
                exact[g]-=exact[m]

        pref=[]
        val=[]
        s=0
        for g in range(1,mx+1):
            if exact[g]:
                s+=exact[g]
                pref.append(s)
                val.append(g)

        return [val[bisect_right(pref,q)] for q in queries]   
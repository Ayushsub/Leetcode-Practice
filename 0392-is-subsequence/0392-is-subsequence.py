class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)

# from collections import defaultdict
# from bisect import bisect_right
# class SubsequenceChecker:
#     def __init__(self,t:str):
#         self.pos=defaultdict(list)
#         for i,ch in enumerate(t):
#             self.pos[ch].append(i)

#     def isSubsequence(self,s:str)->bool:
#         prev=-1
#         for ch in s:
#             if ch not in self.pos:
#                 return False
#             idx=bisect_right(self.pos[ch],prev)
#             if idx==len(self.pos[ch]):
#                 return False
#             prev=self.pos[ch][idx]
#         return True

#bisect_right(arr, x) returns the position where x would be inserted to the right of any existing x. In other words, it gives you the index of the first element strictly greater than x
        
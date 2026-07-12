class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=arr.copy()
        s.sort()
        d={}
        for i in range(len(arr)):
            if s[i] not in d:
                d[s[i]]=len(d)+1
        
        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr

"""
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}

        for num in sorted(arr):
            if num not in rank:
                rank[num] = len(rank) + 1

        return [rank[num] for num in arr]


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}

        for i, num in enumerate(sorted(set(arr)), 1):
            rank[num] = i

        return [rank[num] for num in arr]
"""

        
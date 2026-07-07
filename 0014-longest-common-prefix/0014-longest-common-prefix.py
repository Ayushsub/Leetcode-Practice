class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=strs[0]
        for i in range(1,len(strs)):
            j=0
            while j<min(len(a),len(strs[i])) and a[j]==strs[i][j]:
                j+=1
            a=a[:j]

            if a=="":
                return ""

        return a
            
"""
Sort the strings first.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first = strs[0]
        last = strs[-1]

        i = 0
        while i < min(len(first), len(last)) and first[i] == last[i]:
            i += 1

        return first[:i]

Why does this work?
After sorting,

flower
flow
flight

becomes

flight
flow
flower

The common prefix of the first and last strings is the common prefix of the whole array.

Time: O(n log n + m)

Usually slower because of sorting.


"""
        
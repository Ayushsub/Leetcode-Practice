class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        m=-1
        c=0
        for l,r in intervals:
            if r>m:
                c+=1
                m=r
        return c 
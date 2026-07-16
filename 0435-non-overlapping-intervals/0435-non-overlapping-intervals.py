class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count=0
        prev_end=intervals[0][1]
        for i in range(1,len(intervals)):
            #overlap
            if intervals[i][0]<prev_end:
                count+=1
            else:
                prev_end=intervals[i][1]

        return count
        #Always keep interval with: smaller ending time, because it leaves more space for future intervals.


class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        i=j=0
        ans=[]
        while i<len(series1) or j<len(series2):
            if j==len(series2) or (i<len(series1) and series1[i][0]<series2[j][0]):
                t=series1[i][0]
            elif i==len(series1) or series2[j][0]<series1[i][0]:
                t=series2[j][0]
            else:
                t=series1[i][0]
            while i<len(series1) and series1[i][0]<t:
                i+=1
            while j<len(series2) and series2[j][0]<t:
                j+=1
            v1=series1[i][1] if i<len(series1) else 0
            v2=series2[j][1] if j<len(series2) else 0
            ans.append([t,v1+v2])
            if i<len(series1) and series1[i][0]==t:
                i+=1
            if j<len(series2) and series2[j][0]==t:
                j+=1
        return ans
from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        r=Counter(tuple(row) for row in grid)
        c=Counter()
        n=len(grid)
        for j in range(n):
            col=[]
            for i in range(n):
                col.append(grid[i][j])
            c[tuple(col)]+=1
        #c=Counter(tuple(grid[i][j]for i in range(len(grid)))for j in range(len(grid)))
        ans=0
        for k,v in r.items():
            ans+=v*c[k]
        return ans
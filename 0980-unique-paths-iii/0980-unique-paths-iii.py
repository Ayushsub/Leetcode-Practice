class Solution:
    def uniquePathsIII(self, grid: List[List[int]]):
        rows=len(grid)
        cols=len(grid[0])
        total=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!=-1:
                    total+=1
                if grid[i][j]==1:
                    sr=i
                    sc=j
        result=0
        def backtrack(r,c,visited):
            nonlocal result #Use the result from the outer function, not create a new one
            if(r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==-1 or (r,c) in visited):
                return
            visited.add((r,c))
            if(grid[r][c]==2):
                if(len(visited)==total):
                    result+=1
            else:
                backtrack(r+1,c,visited)
                backtrack(r-1,c,visited)
                backtrack(r,c+1,visited)
                backtrack(r,c-1,visited)
            visited.remove((r,c))
        backtrack(sr,sc,set())
        return result
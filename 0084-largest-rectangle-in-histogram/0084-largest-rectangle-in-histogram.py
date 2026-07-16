class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        #Previous Smaller
        ps=[-1]*n
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            ps[i]=stack[-1] if stack else -1
            stack.append(i)

        #Next Smaller
        ns=[n]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            ns[i]=stack[-1] if stack else n
            stack.append(i)
        ans=0
        for i in range(n):
            width=ns[i]-ps[i]-1
            ans=max(ans,width*heights[i])

        return ans


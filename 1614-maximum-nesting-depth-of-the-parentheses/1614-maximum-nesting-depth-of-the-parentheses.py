class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        maxCount=0
        for ch in s:
            if ch=='(':
                count+=1
                maxCount=max(maxCount,count)
            elif ch==')':
                count-=1
        return maxCount
        
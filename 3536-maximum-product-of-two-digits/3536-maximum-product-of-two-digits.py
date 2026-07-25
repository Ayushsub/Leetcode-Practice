class Solution:
    def maxProduct(self, n: int) -> int:
        a=[]
        while n:
            a.append(n%10)
            n//=10
        a.sort(reverse=True)
        return a[0]*a[1]
        
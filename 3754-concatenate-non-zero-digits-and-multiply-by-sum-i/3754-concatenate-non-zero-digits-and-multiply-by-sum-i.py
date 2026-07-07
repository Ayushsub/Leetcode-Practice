class Solution:
    def sumAndMultiply(self, n: int) -> int:
        a=str(n)
        b=""
        sum=0
        for i in range(len(a)):
            if a[i]!="0":
                b+=a[i]
                sum+=int(a[i])
        if b=="":
            return 0
        
        return sum*int(b)
        
        
        
class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        h=n//2
        d=0
        lq=rq=0
        for i in range(h):
            if num[i]=='?':
                lq+=1
            else:
                d+=int(num[i])
        for i in range(h,n):
            if num[i]=='?':
                rq+=1
            else:
                d-=int(num[i])
        if lq==rq:
            return d!=0
        if (lq-rq)%2:
            return True
        return d*2!=9*(rq-lq)
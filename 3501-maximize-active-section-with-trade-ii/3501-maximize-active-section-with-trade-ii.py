from typing import List
from bisect import bisect_left

class SegTree:
    def __init__(self,arr):
        self.n=1
        while self.n<len(arr):
            self.n<<=1
        self.tree=[0]*(2*self.n)
        for i in range(len(arr)):
            self.tree[self.n+i]=arr[i]
        for i in range(self.n-1,0,-1):
            self.tree[i]=max(self.tree[2*i],self.tree[2*i+1])

    def query(self,l,r):
        l+=self.n
        r+=self.n
        res=0
        while r-l>1:
            if l%2==0:
                res=max(res,self.tree[l+1])
            if r%2==1:
                res=max(res,self.tree[r-1])
            l//=2
            r//=2
        return res

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n=len(s)
        flip=[]
        ones=1
        if s[0]=='0':
            flip.append(0)
            ones-=1
        for i in range(1,n):
            if s[i]!=s[i-1]:
                flip.append(i)
            if s[i]=='1':
                ones+=1
        if s[-1]=='0':
            flip.append(n)
        gain=[]
        for j in range(3,len(flip),2):
            gain.append((flip[j]-flip[j-1])+(flip[j-2]-flip[j-3]))
        seg=SegTree(gain)
        ans=[]
        for l,r in queries:
            lPos=bisect_left(flip,l+1)
            rPos=bisect_left(flip,r+1)
            change=0
            if (rPos-lPos<2)or((rPos-lPos==2)and(lPos%2==0)):
                change=0
            elif rPos-lPos==2:
                change=(r+1-flip[rPos-1])+(flip[lPos]-l)
            elif rPos-lPos==3:
                if lPos%2==0:
                    change=(r+1-flip[rPos-1])+(flip[lPos+1]-flip[lPos])
                else:
                    change=(flip[rPos-1]-flip[lPos+1])+(flip[lPos]-l)
            else:
                if lPos%2==1:
                    change=max(change,(flip[lPos+2]-flip[lPos+1])+(flip[lPos]-l))
                    lPos+=1
                if rPos%2==1:
                    change=max(change,(r+1-flip[rPos-1])+(flip[rPos-2]-flip[rPos-3]))
                    rPos-=1
                change=max(change,seg.query(lPos//2-1,rPos//2-1))
            ans.append(ones+change)
        return ans
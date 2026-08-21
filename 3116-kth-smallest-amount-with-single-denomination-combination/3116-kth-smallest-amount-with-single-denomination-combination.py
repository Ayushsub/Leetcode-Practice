from typing import List
from math import gcd
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        a=[]
        for c in coins:
            if not any(c%x==0 for x in a):
                a.append(c)
        n=len(a)
        def lcm(x,y):
            return x//gcd(x,y)*y
        def count(x):
            ans=0
            for mask in range(1,1<<n):
                m=1
                bits=0
                for i in range(n):
                    if mask&(1<<i):
                        bits+=1
                        m=lcm(m,a[i])
                        if m>x:
                            break
                else:
                    if bits&1:
                        ans+=x//m
                    else:
                        ans-=x//m
            return ans
        lo=1
        hi=k*a[0]
        while lo<hi:
            mid=(lo+hi)//2
            if count(mid)>=k:
                hi=mid
            else:
                lo=mid+1
        return lo
import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        es=n*(n+1)
        t=2*n
        ts=t*(t+1)//2
        os=ts-es
        return math.gcd(os,es)


"""
def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

Observation

Sum of the first n odd numbers:
1+3+5+⋯=n^2

Sum of the first n even numbers:
2+4+6+⋯+2n=n(n+1)

So we need
gcd(n^2,n(n+1))

Since consecutive numbers are coprime,
gcd(n,n+1)=1

Therefore,
gcd(n^2,n(n+1))=n⋅gcd(n,n+1)=n
So the answer is simply n.
"""
        
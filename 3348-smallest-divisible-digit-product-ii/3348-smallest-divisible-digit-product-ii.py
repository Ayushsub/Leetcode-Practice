import math

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp=t
        for i in range(2,10):
            while temp%i==0:
                temp//=i
        if temp>1:
            return "-1"

        n=len(num)
        rem=[0]*(n+1)
        rem[0]=t
        pos=n-1
        a=list(num)

        for i in range(n):
            if a[i]=="0":
                pos=i
                break
            rem[i+1]=rem[i]//math.gcd(rem[i],int(a[i]))

        if rem[n]==1:
            return num

        for i in range(pos,-1,-1):
            while True:
                a[i]=str(int(a[i])+1)
                if int(a[i])>9:
                    break
                cur=rem[i]//math.gcd(rem[i],int(a[i]))
                k=9
                for j in range(n-1,i,-1):
                    while cur%k:
                        k-=1
                    cur//=k
                    a[j]=str(k)
                if cur==1:
                    return "".join(a)

        ans=[]
        x=t
        for i in range(9,1,-1):
            while x%i==0:
                ans.append(str(i))
                x//=i

        s="".join(ans)
        s+="1"*max(n+1-len(s),0)
        return s[::-1]
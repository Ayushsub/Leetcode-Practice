class Solution:
    def compress(self, chars: List[str]) -> int:
        ans=[]
        i=0
        n=len(chars)
        while i<n:
            ch=chars[i]
            cnt=0
            while i<n and chars[i]==ch:
                cnt+=1
                i+=1
            ans.append(ch)
            if cnt>1:
                ans.extend(str(cnt))
        for i in range(len(ans)):
            chars[i]=ans[i]
        return len(ans)




        
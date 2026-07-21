class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones=s.count("1")
        t="1"+s+"1"
        chars=[]
        lens=[]
        for ch in t:
            if chars and chars[-1]==ch:
                lens[-1]+=1
            else:
                chars.append(ch)
                lens.append(1)
        ans=ones
        for i in range(1,len(chars)-1):
            if chars[i]=="1" and chars[i-1]=="0" and chars[i+1]=="0":
                gain=lens[i-1]+lens[i+1]
                ans=max(ans,ones+gain)
        return ans
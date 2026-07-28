class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        a=''
        w1=len(word1)
        w2=len(word2)
        x=min(w1,w2)
        for l in range(x*2):
            if i>j:
                a+=word2[j]
                j+=1
            else:
                a+=word1[i]
                i+=1
        if w1>w2:
            a+=word1[x:]
        else:
            a+=word2[x:]
        return a
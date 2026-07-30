class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        d1={}
        d2={}
        for i in word1:
            d1[i]=d1.get(i,0)+1
        for i in word2:
            d2[i]=d2.get(i,0)+1
        return set(d1)==set(d2) and sorted(d1.values())==sorted(d2.values())
        
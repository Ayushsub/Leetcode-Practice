class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset=set(words)
        ans=[]
        def canForm(word):
            n=len(word)
            dp=[False]*(n+1)
            dp[0]=True
            for i in range(1,n+1):
                for j in range(i):
                    if dp[j] and word[j:i] in wordset:
                        dp[i]=True
                        break
            return dp[n]
        for word in words:
            wordset.remove(word)
            if canForm(word):
                ans.append(word)
            wordset.add(word)
        return ans
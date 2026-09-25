class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def dfs():
            res={""}
            while i[0]<len(expression) and expression[i[0]]!="}":
                if expression[i[0]]==",":
                    i[0]+=1
                    res|=dfs()
                elif expression[i[0]]=="{":
                    i[0]+=1
                    cur=dfs()
                    i[0]+=1
                    res={a+b for a in res for b in cur}
                else:
                    cur={expression[i[0]]}
                    i[0]+=1
                    res={a+b for a in res for b in cur}
            return res
        i=[0]
        return sorted(dfs())
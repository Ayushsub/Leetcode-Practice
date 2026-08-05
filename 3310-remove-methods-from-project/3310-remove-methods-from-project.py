class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g=[[]for _ in range(n)]
        for a,b in invocations:
            g[a].append(b)
        vis=[False]*n
        st=[k]
        vis[k]=True
        while st:
            u=st.pop()
            for v in g[u]:
                if not vis[v]:
                    vis[v]=True
                    st.append(v)
        for a,b in invocations:
            if not vis[a]and vis[b]:
                return list(range(n))
        return[i for i in range(n) if not vis[i]]
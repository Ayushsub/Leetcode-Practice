class Solution:
    def findCheapestPrice(self,n:int,flights:List[List[int]],src:int,dst:int,k:int)->int:
        INF=float('inf')
        dp=[INF]*n
        dp[src]=0
        for _ in range(k+1):
            ndp=dp[:]
            for u,v,w in flights:
                if dp[u]!=INF and dp[u]+w<ndp[v]:
                    ndp[v]=dp[u]+w
            dp=ndp
        return-1 if dp[dst]==INF else dp[dst]

# from heapq import heappush,heappop
# class Solution:
#     def findCheapestPrice(self,n:int,flights:List[List[int]],src:int,dst:int,k:int)->int:
#         g=[[]for _ in range(n)]
#         for u,v,w in flights:
#             g[u].append((v,w))
#         INF=float('inf')
#         dist=[[INF]*(k+2)for _ in range(n)]
#         dist[src][0]=0
#         pq=[(0,src,0)]
#         while pq:
#             c,u,s=heappop(pq)
#             if u==dst:
#                 return c
#             if c>dist[u][s]:
#                 continue
#             if s==k+1:
#                 continue
#             for v,w in g[u]:
#                 if c+w<dist[v][s+1]:
#                     dist[v][s+1]=c+w
#                     heappush(pq,(c+w,v,s+1))
#         return-1
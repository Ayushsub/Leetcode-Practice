from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited=[False]*n
        ans=0

        def dfs(node,component):
            visited[node]=True
            component.append(node)

            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei,component)

        for i in range(n):
            if not visited[i]:
                component=[]
                dfs(i,component)
                size=len(component)
                complete=True
                for node in component:
                    if len(graph[node])!=size-1:
                        complete=False
                        break
                if complete:
                    ans+=1

        return ans
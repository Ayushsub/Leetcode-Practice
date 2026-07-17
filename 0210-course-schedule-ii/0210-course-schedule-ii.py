from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Graph + indegree
        graph = defaultdict(list)
        indegree = [0] * numCourses
        # Build graph
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        # Start with courses having 0 prerequisite
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        order = []
        while q:
            course = q.popleft()
            order.append(course)
            # Reduce indegree of neighbors
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        # If all courses completed
        if len(order) == numCourses:
            return order

        return []



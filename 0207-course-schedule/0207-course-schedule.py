class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:            # Detecting a Cycle as 0 is not visited , 1 is visitng and 2 is visited
                return False
            if visited[course] == 2:            #Sucesfully visited everything so complete and not a cycle 
                return True
            visited[course] = 1

            for nei in graph[course]:
                if not dfs(nei):
                    return False
                
            
            visited[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True



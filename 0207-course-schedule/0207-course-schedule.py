class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]  # Create an empty adjacency list

        for a, b in prerequisites:
            graph[b].append(a)  # Add an edge from prerequisite b to course a

        visited = [0] * numCourses  # 0 = not visited, 1 = exploring, 2 = completed

        def dfs(course):
            if visited[course] == 1:  # Course is already being explored, so cycle found
                return False

            if visited[course] == 2:  # Course is already completely explored
                return True

            visited[course] = 1  # Mark course as currently exploring

            for nei in graph[course]:  # Explore every neighbour of the current course
                if not dfs(nei):  # If any neighbour has a cycle
                    return False  # Return False immediately

            visited[course] = 2  # Mark course as completely explored
            return True  # No cycle found in this path

        for i in range(numCourses):  # Check every course, including disconnected ones
            if not dfs(i):  # If any course leads to a cycle
                return False

        return True  # All courses can be completed
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        res = []
        path = [0]
        n = len(graph)

        def dfs(node):
            if node == n-1:
                res.append(path[:])
                return
            
            for nei in graph[node]:
                path.append(nei)
                dfs(nei)
                path.pop()
        
        dfs(0)
        return res
        
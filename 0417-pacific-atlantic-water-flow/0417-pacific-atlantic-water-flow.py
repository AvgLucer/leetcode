class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(r, c, visited):
            stack = [(r, c)]

            while stack:
                r, c = stack.pop()

                if (r, c) in visited:
                    continue

                visited.add((r, c))

                for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < m and 0 <= nc < n
                        and (nr, nc) not in visited
                        and heights[nr][nc] >= heights[r][c]):

                        stack.append((nr, nc))

        # Pacific: top and left edges
        for r in range(m):
            dfs(r, 0, pacific)

        for c in range(n):
            dfs(0, c, pacific)

        # Atlantic: bottom and right edges
        for r in range(m):
            dfs(r, n-1, atlantic)

        for c in range(n):
            dfs(m-1, c, atlantic)

        # Intersection of both sets
        return [[r, c] for r, c in pacific & atlantic]
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old = image[sr][sc]
        if old == color: return image
        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or image[r][c] != old: return
            image[r][c] = color
            for dr,dc in [(1,0) , (-1,0) , (0,1),(0,-1) ]: dfs(r+dr,c+dc)
        
        dfs(sr,sc)
        return image


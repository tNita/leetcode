class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        ans = 0

        def dfs(r: int, c: int) -> int:
            # 再帰
            # if r < 0 or r >= height or c < 0 or c >= width or grid[r][c] == 0:
            #     return 0
            # # 訪問済みに
            # grid[r][c] = 0
            # return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)

            area = 0
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                if grid[r][c] == 1:
                    area += 1
                    # 訪問済みに
                    grid[r][c] = 0
                    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        # 範囲外なのでスキップ
                        if nr >= 0 and nr < height and nc >= 0 and nc < width:
                            stack.append((nr, nc))
            return area

        for i in range(height):
            for j in range(width):
                ans = max(ans, dfs(i, j))
        return ans

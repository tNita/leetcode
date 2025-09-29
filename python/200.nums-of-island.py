class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height, width = len(grid), len(grid[0])
        ans = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    ans += 1
                    # ここを起点に陸続きの箇所を全て訪問する
                    stack = [(i, j)]
                    while stack:
                        m, n = stack.pop()
                        grid[m][n] = "0"
                        for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if (
                                -1 < m + dh < height
                                and -1 < n + dw < width
                                and grid[m + dh][n + dw] == "1"
                            ):
                                stack.append((m + dh, n + dw))
        return ans

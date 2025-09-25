class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        # def factorial(x: int) -> int:
        #     if x == 1: return 1
        #     return x * factorial(x-1)
        # return factorial(m+n-2) // (factorial(m-1) * factorial(n-1))

        # DP
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dp[i][n - 1] = 1
        for j in range(n):
            dp[m - 1][j] = 1

        stack = [(0, 0)]
        while stack:
            d, r = stack.pop()
            if dp[d][r + 1] == 0:
                stack.append((d, r))
                stack.append((d, r + 1))
                continue
            if dp[d + 1][r] == 0:
                stack.append((d, r))
                stack.append((d + 1, r))
                continue

            dp[d][r] = dp[d][r + 1] + dp[d + 1][r]
        return dp[0][0]

        # DP（右下から）
        # dp = [[1] * n for _ in range(m)]

        # # 右下から左上に向かって計算
        # for i in range(m - 2, -1, -1):
        #     for j in range(n - 2, -1, -1):
        #         dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        # return dp[0][0]

        # DP（右下から、1次元）
        # dp = [1] * n
        # for _ in range(m - 1):
        #     for j in range(n - 2, -1, -1):
        #         dp[j] += dp[j + 1]
        # return dp[0]

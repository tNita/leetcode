class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        def factorial(x: int) -> int:
            if x == 1:
                return 1
            return x * factorial(x - 1)

        return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))

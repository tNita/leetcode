class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -1 * n)
        # 再帰
        # if n == 0:
        #     return 1

        # half = self.myPow(x, n // 2)
        # if n % 2 == 0:
        #     return half * half
        # else:
        #     return half * half * x

        # ループ
        # 2^13 = 2^(2*3) * 2^(2*2) * 2^1
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans *= x
            x *= x
            n = n // 2
        return ans

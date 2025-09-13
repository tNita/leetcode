class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # n行目のk番目へはk-1の2進数表現で頭から0（左）、1（右）とした道順
        # 右に行けば反転するのでk-1の二進数表現の1の数の偶奇による
        # return (k - 1).bit_count() & 1

        # 再帰
        # kが奇数→左子、,kが偶数→右子
        # 親は k +1  // 2
        if n == 1:
            return 0

        parent = self.kthGrammar(n - 1, (k + 1) // 2)
        return parent if k % 2 == 1 else 1 - parent

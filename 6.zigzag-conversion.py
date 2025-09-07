class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 周期（自分の案）
        if numRows == 1:
            return s
        arr = [""] * numRows
        bunch = 2 * numRows - 2
        for i, c in enumerate(s):
            k = i % bunch
            if k < numRows:
                arr[k] += c
            else:
                ro = k - numRows
                arr[numRows - 1 - 1 - ro] += c
        return "".join(arr)

        # 方向フラグ
        # if numRows == 1:
        #     return s
        # arr = [''] * numRows
        # cur = 0
        # step = 1
        # for c in s:
        #     arr[cur] += c
        #     if cur == 0:
        #         step = 1
        #     elif cur == numRows -1:
        #         step = -1
        #     cur += step
        # return "".join(arr)

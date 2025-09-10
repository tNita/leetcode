class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # どんな正しい括弧列も必ず内側に () を含み、それを取り除けばより小さい正しい括弧列になる。
        # 小さい正しい括弧列に () を挿入することで全ての正しい括弧列を得られる。
        # start = ["()"]
        # if n == 1:
        #     return start
        # pattern = set(start)
        # for i in range(2, n + 1):
        #     newPattern = set([])
        #     for p in pattern:
        #         for i in range(len(p) + 1):
        #             newPattern.add(p[:i] + "()" + p[i:])
        #     pattern = newPattern
        #     print(pattern)
        # return list(pattern)

        # バックトラッキング
        res = []

        def backTrack(cur: str, openCnt: int, closeCnt: int) -> None:
            if len(cur) == 2 * n:
                res.append(cur)
                return

            if openCnt < n:
                backTrack(cur + "(", openCnt + 1, closeCnt)

            if closeCnt < openCnt:
                backTrack(cur + ")", openCnt, closeCnt + 1)

        backTrack("", 0, 0)
        return res

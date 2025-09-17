class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def check(start: int, remain: int, path: List[int]) -> None:
            if remain == 0:
                ans.append(path.copy())  # 後で中身が変わらないようにコピーを追加

            if remain <= 0:
                return

            for i in range(start, len(candidates)):
                if remain < candidates[i]:
                    break
                path.append(candidates[i])
                check(i, remain - candidates[i], path)
                path.pop()

        check(0, target, [])
        return ans

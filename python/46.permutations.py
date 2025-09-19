class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        ans = []
        subP = self.permute(nums[1:])
        for x in subP:
            for i in range(len(x) + 1):
                s = x.copy()
                s.insert(i, nums[0])
                ans.append(s)
        return ans

        # バックトラッキング
        # ans = []
        # # nums[0:first) はすでに確定した部分列
        # def backtrack(first: int) -> None:
        #     if first == len(nums):
        #         ans.append(nums[:])
        #         return
        #     for i in range(first, len(nums)):
        #         nums[first], nums[i] = nums[i], nums[first]  # 候補を先頭側に
        #         backtrack(first + 1)                         # 次の位置へ
        #         nums[first], nums[i] = nums[i], nums[first]  # ロールバック
        # backtrack(0)
        # return ans

        # iterator tool使う
        # ans = []
        # # リストから順列を生成
        # for p in itertools.permutations(nums, len(nums)):
        #     ans.append(p)

        # return ans

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for x in nums:
            # 既存の部分集合に x を足した新集合を全部作って追加
            ans += [cur + [x] for cur in ans]
        return ans

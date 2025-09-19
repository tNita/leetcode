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

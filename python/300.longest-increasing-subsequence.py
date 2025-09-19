class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length
        for i in range(1, length):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

        # 二分探索で
        # tails = []  # 長さkの増加部分列の末尾最小値を tails[k-1] に保持
        # for n in nums:
        #     i = bisect_left(tails, n)  # x を置ける最左位置
        #     if i == len(tails):
        #         tails.append(n)
        #     else:
        #         tails[i] = n
        # return len(tails)

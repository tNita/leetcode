class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = []
        for i, n in enumerate(nums):
            if i == 0:
                maxsum.append(n)
                continue
            # 一つ前のsubarrayの最大和
            maxsubarr = maxsum[i - 1]
            if maxsubarr < 0:
                maxsum.append(n)
            else:
                maxsum.append(n + maxsubarr)
        return max(maxsum)

        # 別解
        # current_sum = nums[0]
        # max_sum = nums[0]
        # for n in nums[1:]:
        #     current_sum = max(n, current_sum + n)
        #     max_sum = max(max_sum, current_sum)
        # return max_sum

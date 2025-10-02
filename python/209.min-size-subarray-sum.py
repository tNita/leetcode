class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float("inf")
        s = 0
        left = 0
        for right in range(n):
            s += nums[right]
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return 0 if ans == float("inf") else ans

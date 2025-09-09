#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2pointer法を使ってみる
        # numsの要素数は変わっていないことに注意
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1

        for i in range(left, len(nums)):
            nums[i] = 0


# @lc code=end

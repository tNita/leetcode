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
        pos = len(nums) - 1
        while pos > -1:
            if nums[pos] == 0:
                nums.append(nums.pop(pos))
            pos -= 1


# @lc code=end

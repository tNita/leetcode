#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while right > left:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        ## 見つからなかった場合 or 要素が一つの時
        return left if nums[left] >= target else left + 1


# @lc code=end

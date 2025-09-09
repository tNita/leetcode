# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        left = 0
        right = len(nums) - 1
        middle = (right - left) // 2

        leftNode = self.sortedArrayToBST(nums[left:middle])
        rightNode = self.sortedArrayToBST(nums[middle + 1 : right + 1])
        return TreeNode(nums[middle], leftNode, rightNode)

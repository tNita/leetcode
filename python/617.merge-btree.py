# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 == None:
            return root2
        if root2 == None:
            return root1

        left = self.mergeTrees(root1.left, root2.left)
        right = self.mergeTrees(root1.right, root2.right)
        return TreeNode(root1.val + root2.val, left, right)

        # if root1 == None:
        #     return root2
        # if root2 == None:
        #     return root1

        # stack = [(root1, root2)]
        # while stack:
        #     n1, n2 = stack.pop()
        #     # n1、n2ともにNoneではない
        #     n1.val += n2.val
        #     if n1.left and n2.left:
        #         stack.append((n1.left, n2.left))
        #     elif n2.left:
        #         n1.left = n2.left # 接続

        #     if n1.right and n2.right:
        #         stack.append((n1.right, n2.right))
        #     elif n2.right:
        #         n1.right = n2.right # 接続
        # return root1

        # if root1 == None:
        #     return root2
        # if root2 == None:
        #     return root1

        # queue = deque([[root1, root2]])
        # while queue:
        #     n1, n2 = queue.popleft()
        #     n1.val += n2.val

        #     if n1.left and n2.left:
        #         queue.append([n1.left, n2.left])
        #     elif n2.left:
        #         n1.left = n2.left

        #     if n1.right and n2.right:
        #         queue.append([n1.right, n2.right])
        #     elif n2.right:
        #         n1.right = n2.right
        # return root1

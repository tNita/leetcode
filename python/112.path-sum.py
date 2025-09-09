# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        # DFS
        stack = [(root, root.val)]
        while stack:
            n, s = stack.pop()

            # nがleaf node のとき
            if n.left is None and n.right is None:
                if s == targetSum:
                    return True
                continue

            if n.left:
                stack.append((n.left, s + n.left.val))
            if n.right:
                stack.append((n.right, s + n.right.val))

        return False

        # BFS
        # queue = deque([[root, root.val]])
        # while queue:
        #     n, s = queue.popleft()

        #     # nがleaf node のとき
        #     if n.left is None and n.right is None:
        #         if s == targetSum:
        #             return True
        #         continue

        #     if n.left:
        #         queue.append([n.left, s + n.left.val])
        #     if n.right:
        #         queue.append([n.right, s + n.right.val])

        # return False

        # REC
        # if root.left is None and root.right is None:
        #     return targetSum == root.val
        # return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

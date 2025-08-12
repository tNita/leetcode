# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # DFS
        # if root is None:
        #     return 0

        # stack = [(root, 1)]
        # max_depth = 0

        # while stack:
        #     node, depth = stack.pop()
        #     max_depth = max(max_depth, depth)
        #     if node.left:
        #         stack.append((node.left, depth + 1))
        #     if node.right:
        #         stack.append((node.right, depth + 1))

        # return max_depth

        # BFS
        # if root is None:
        #     return 0

        # depth = 0
        # queue = deque([root])

        # while queue:
        #     depth += 1
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        # return depth

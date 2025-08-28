# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # BFS
        queue = deque([[root, 1]])
        while queue:
            n, d = queue.popleft()
            if n.left is None and n.right is None:
                return d
            if n.left:
                queue.append([n.left, d + 1])
            if n.right:
                queue.append([n.right, d + 1])

        # 再帰

        # leftDepth  = self.minDepth(root.left)
        # rightDepth = self.minDepth(root.right)

        # if leftDepth != 0 and rightDepth != 0:
        #     return 1 + min(leftDepth, rightDepth)

        # if leftDepth == 0:
        #     return 1 + rightDepth

        # return 1 + leftDepth

        # DFS
        # stack = [(root, 1)]
        # depth = float('inf')
        # while stack:
        #     n, d = stack.pop()
        #     if n.right is None and n.left is None:
        #         if d < depth:
        #             depth = d
        #         continue

        #     # 枝刈り（既知の最短以上は探索しない）
        #     if d + 1 >= depth:
        #         continue

        #     if n.right:
        #         stack.append((n.right, d+1))
        #     if n.left:
        #         stack.append((n.left, d+1))
        # return depth

        # DFSは必ず全捜査になるが、BFSはリーフを見つけた時点で捜査が終了するので全操作にならない。BFSが良い

1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
9        self.result = 0
10
11        def dfs(root):
12            if not root:
13                return 0
14            left = dfs(root.left)
15            right = dfs(root.right)
16            self.result = max(self.result, left + right)
17            return 1 + max(left, right)
18
19        dfs(root)
20        return self.result
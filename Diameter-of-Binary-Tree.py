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
11        def dfs(curr):
12            if not curr:
13                return 0
14            left = dfs(curr.left)
15            right = dfs(curr.right)
16            self.result = max(self.result, left + right)
17            return 1 + max(left, right)
18
19
20        dfs(root)
21        return self.result
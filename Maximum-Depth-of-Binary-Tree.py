1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        curr = 0
10        def depth(root):
11            if not root:
12                return 0
13            l = depth(root.left)
14            l += 1
15            r = depth(root.right)
16            r += 1
17            return max(l, r)
18
19        max_depth = depth(root)
20        return max_depth
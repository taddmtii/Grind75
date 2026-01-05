1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        balanced = True
10
11        def height(root):
12            nonlocal balanced
13
14            if not root:
15                return 0
16            
17            l_height = height(root.left)
18            r_height = height(root.right)
19
20            if abs(l_height - r_height) > 1:
21                balanced = False
22                return 0
23            
24            return 1 + max(l_height, r_height)
25
26        height(root)
27        return balanced
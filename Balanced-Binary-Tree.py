1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        balanced = [True]
10
11        def height(curr):
12            if not curr:
13                return 0
14        
15            left = height(curr.left)
16            right = height(curr.right)
17            if abs(left - right) > 1:
18                balanced[0] = False
19                return 0
20
21            return 1 + max(left, right) 
22
23        height(root)
24        return balanced[0]
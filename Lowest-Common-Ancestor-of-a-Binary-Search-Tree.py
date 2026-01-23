1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        curr = root
11
12        while curr:
13            if p.val > curr.val and q.val > curr.val:
14                curr = curr.right
15            elif p.val < curr.val and q.val < curr.val:
16                curr = curr.left
17            else:
18                return curr
19
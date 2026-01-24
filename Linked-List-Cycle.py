1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        if not head:
10            return False
11
12        slow, fast = head, head.next
13
14        while slow and fast and fast.next:
15            if slow == fast:
16                return True
17            slow = slow.next
18            fast = fast.next.next
19        return False
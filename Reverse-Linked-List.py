1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head:
9            return None
10        prev, curr = None, head
11        while curr != None:
12            temp = curr.next
13            curr.next = prev
14            prev, curr = curr, temp
15        return prev
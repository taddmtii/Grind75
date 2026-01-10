1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode()
9        merged = dummy
10
11        while list1 and list2:
12            if list1.val > list2.val:
13                merged.next = list2
14                list2 = list2.next
15            elif list1.val <= list2.val:
16                merged.next = list1
17                list1 = list1.next
18            merged = merged.next
19
20        if list1:
21            merged.next = list1
22        elif list2:
23            merged.next = list2
24
25        return dummy.next
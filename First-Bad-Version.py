1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        L, R = 0, n
7        while L <= R:
8            mid = L + (R - L) // 2
9            if isBadVersion(mid):
10                R = mid - 1
11            else:
12                L = mid + 1
13        return L
14
1class Solution:
2    def longestPalindrome(self, s: str) -> int:
3        count = defaultdict(int)
4        res = 0
5
6        for c in s:
7            count[c] += 1
8            # even?
9            if count[c] % 2 ==0:
10                res += 2
11        
12        for cnt in count.values():
13            # odd?
14            if cnt % 2:
15                res += 1
16                break
17
18        return res
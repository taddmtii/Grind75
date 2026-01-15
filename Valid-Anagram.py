1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5        s_map = Counter(s)
6        t_map = Counter(t)
7
8        for s in s_map:
9            if s not in t_map or t_map[s] != s_map[s]:
10                return False
11        return True
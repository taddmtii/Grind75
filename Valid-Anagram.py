1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5        s_map = Counter(s)
6        t_map = Counter(t)
7        for key, value in s_map.items():
8            if key not in t_map or t_map[key] != value:
9                return False
10
11        return True
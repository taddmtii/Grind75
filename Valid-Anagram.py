1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        s_map = Counter(s)
4        t_map = Counter(t)
5
6        return s_map == t_map
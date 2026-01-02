class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = Counter(s)
        t_map = Counter(t)
        for key, value in s_map.items():
            if key not in t_map or t_map[key] != value:
                return False

        return True

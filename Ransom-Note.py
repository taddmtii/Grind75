1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        mag_dict = Counter(magazine)
4        for ch in ransomNote:
5            if mag_dict[ch]:
6                mag_dict[ch] -= 1
7            else:
8                return False
9        return True
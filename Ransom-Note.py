1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        magazine_dict = Counter(magazine)
4
5        for ch in ransomNote:
6            if ch in magazine_dict and magazine_dict[ch] != 0:
7                magazine_dict[ch] -= 1
8            else:
9                return False
10        return True
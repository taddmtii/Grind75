1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        cleaned = ""
4        for ch in s:
5            if ch.isalnum():
6                cleaned += ch.lower()
7        
8        l, r = 0, len(cleaned) - 1
9
10        for _ in range(len(cleaned)):
11            if cleaned[l] == cleaned[r]:
12                l += 1
13                r -= 1
14            else:
15                return False
16        return True
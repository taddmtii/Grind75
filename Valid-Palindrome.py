1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        cleaned = ""
4        for ch in s:
5            if ch.isalnum():
6                cleaned += ch.lower()
7        
8        l, r = 0, len(cleaned) - 1
9
10        while l <= r:
11            if cleaned[l] != cleaned[r]:
12                return False
13            l += 1
14            r -= 1
15        return True
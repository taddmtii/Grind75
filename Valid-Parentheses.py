1class Solution:
2    def isValid(self, s: str) -> bool:
3        closing = {"}": "{", ")": "(", "]": "["}
4        stack = []
5        if len(s) <= 1:
6            return False
7
8        for ch in s:
9            if ch in ["(", "{", "["]:
10                stack.append(ch)
11            else:
12                if stack:
13                    elem = stack.pop()
14                    if elem != closing[ch]:
15                        return False
16                else:
17                    return False
18    
19        return not stack
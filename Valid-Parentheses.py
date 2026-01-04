1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        closing_brackets = {")": "(", "]": "[", "}": "{"}
5        
6        for symbol in s:
7            if symbol in closing_brackets.values():
8                stack.append(symbol)
9            elif symbol in closing_brackets:
10                if stack and stack[-1] == closing_brackets[symbol]:
11                    stack.pop()
12                else:
13                    return False
14        return stack == []
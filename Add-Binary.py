1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        res = ""
4        carry = 0
5
6        a, b = a[::-1], b[::-1]
7
8        for i in range(max(len(a), len(b))):
9            digitA = int(a[i]) if i < len(a) else 0
10            digitB = int(b[i]) if i < len(b) else 0
11
12            total = digitA + digitB + carry
13            char = str(total % 2)
14            res = char + res
15            carry = total // 2
16        
17        if carry:
18            res = "1" + res
19        
20        return res
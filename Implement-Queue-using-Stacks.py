1class MyQueue:
2
3    def __init__(self):
4        #s1 push
5        #s2 pop
6        self.s1 = []
7        self.s2 = []
8
9    def push(self, x: int) -> None:
10        self.s1.append(x)
11
12    def pop(self) -> int:
13        if not self.s2:
14            while self.s1:
15                self.s2.append(self.s1.pop())
16        return self.s2.pop()
17
18    def peek(self) -> int:
19        if not self.s2:
20            while self.s1:
21                self.s2.append(self.s1.pop())
22        return self.s2[-1]
23
24    def empty(self) -> bool:
25        return max(len(self.s1), len(self.s2)) == 0
26
27
28# Your MyQueue object will be instantiated and called as such:
29# obj = MyQueue()
30# obj.push(x)
31# param_2 = obj.pop()
32# param_3 = obj.peek()
33# param_4 = obj.empty()
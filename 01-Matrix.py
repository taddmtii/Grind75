1class Solution:
2    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
3        ROWS, COLS = len(mat), len(mat[0])
4        directions = [[1,0], [0,1], [-1,0], [0,-1]]
5        res = [[-1 for _ in range(COLS)] for _ in range(ROWS)]
6        visited = set()
7        zeroes = deque()
8
9        # Initialize all zeroes
10        for row in range(ROWS):
11            for col in range(COLS):
12                if mat[row][col] == 0:
13                    res[row][col] = 0
14                    zeroes.append([row, col, 0])
15                    visited.add((row, col))
16        
17        # BFS
18        while zeroes:
19            row, col, dist = zeroes.popleft()
20            for r, c in directions:
21                n_row, n_col = row + r, col + c
22                if 0 <= n_row < ROWS and 0 <= n_col < COLS and (n_row, n_col) not in visited:
23                    res[n_row][n_col] = dist + 1
24                    visited.add((n_row, n_col))
25                    zeroes.append([n_row, n_col, dist + 1])
26        return res
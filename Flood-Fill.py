1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        seen = set()
4        original_color = image[sr][sc]
5        num_rows, num_cols = len(image), len(image[0])
6
7        def dfs(row, col):
8            if (row, col) in seen or row < 0 or row >= num_rows or col < 0 or col >= num_cols:
9                return
10            seen.add((row, col))
11            if image[row][col] == original_color:
12                image[row][col] = color
13                dfs(row + 1, col)
14                dfs(row - 1, col)
15                dfs(row, col + 1)
16                dfs(row, col - 1)
17
18        dfs(sr, sc)
19        return image
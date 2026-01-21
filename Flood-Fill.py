1class Solution:
2    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
3        seen = set()
4        startingColor = image[sr][sc]
5        
6
7        def dfs(row, col):
8            if row >= len(image) or row < 0 or col >= len(image[0]) or col < 0 or (row, col) in seen or image[row][col] != startingColor:
9                return 
10            
11            image[row][col] = color
12            seen.add((row, col))
13            
14            dfs(row + 1, col)
15            dfs(row - 1, col)
16            dfs(row, col + 1)
17            dfs(row, col - 1) 
18        
19
20        dfs(sr, sc)
21        return image
22
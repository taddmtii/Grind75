1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        result = []
4
5        for i in range(len(intervals)):
6            if newInterval[1] < intervals[i][0]:
7                result.append(newInterval)
8                return result + intervals[i:] # append the rest
9            elif newInterval[0] > intervals[i][1]:
10                result.append(intervals[i])
11            else:
12                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
13        
14        result.append(newInterval)
15        return result
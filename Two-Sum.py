1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3            if nums == []:
4                return []
5    
6            nums_map = {}
7
8            # keys are the values, values are the indexes
9            for i in range(len(nums)):
10                nums_map[nums[i]] = i
11            
12            for i in range(len(nums)):
13                diff = target - nums[i]
14                if diff in nums_map and nums_map[diff] != i:
15                    return [i, nums_map[diff]]
16
17
18
19
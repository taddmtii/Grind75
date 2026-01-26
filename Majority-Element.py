1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        nums_map = Counter(nums)
4        majority = len(nums) / 2
5        
6        for elem in nums_map:
7            if nums_map[elem] >= majority:
8                return elem
9        
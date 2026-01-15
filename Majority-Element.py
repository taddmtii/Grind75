1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        nums_map = Counter(nums)
4        n = len(nums) / 2
5        for num in nums:
6            if nums_map[num] > n:
7                return num
8
9
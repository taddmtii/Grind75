1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        nums_map = Counter(nums)
4        for value in nums_map.values():
5            if value > 1:
6                return True
7        return False
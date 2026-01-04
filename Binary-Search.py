1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        left = 0
4        right = len(nums) - 1
5
6        while left <= right:
7            mid = (left + right) // 2
8            if target == nums[mid]:
9                return mid
10            elif target < nums[mid]:
11                right = mid - 1
12            elif target > nums[mid]:
13                left = mid + 1
14        return -1
15        
16
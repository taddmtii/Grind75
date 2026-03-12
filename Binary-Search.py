1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0, len(nums) - 1
4        
5        while (l <= r):
6            mid = (l + r) // 2
7            if target == nums[mid]:
8                return mid
9            elif target < nums[mid]:
10                r = mid - 1
11            else:
12                l = mid + 1
13        return -1
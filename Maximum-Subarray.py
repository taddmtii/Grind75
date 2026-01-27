1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        maxSub = nums[0]
4        curSum = 0
5
6        for n in nums:
7            if curSum < 0:
8                curSum = 0
9            curSum += n
10            maxSub  = max(maxSub, curSum)
11        return maxSub
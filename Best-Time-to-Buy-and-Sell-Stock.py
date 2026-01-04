1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        if len(prices) <= 1:
4            return 0
5        low = prices[0]
6        profit = 0
7        for i in range(len(prices)):
8            if prices[i] <= low:
9                low = prices[i]
10            if prices[i] > low and prices[i] - low > profit:
11                profit = prices[i] - low
12        return profit
13                
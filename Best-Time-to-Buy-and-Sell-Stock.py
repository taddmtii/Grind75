1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        L, R = 0, 1
4        max_profit = 0
5        while R < len(prices):
6            if prices[L] < prices[R]:
7                profit = prices[R] - prices[L]
8                max_profit = max(max_profit, profit)
9            else:
10                L = R
11            R += 1
12        return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        left = 0
        profit = 0

        for right in range(1, n):
            if prices[left] > prices[right]:
                left = right
            profit = max(profit, prices[right] - prices[left])

        return profit

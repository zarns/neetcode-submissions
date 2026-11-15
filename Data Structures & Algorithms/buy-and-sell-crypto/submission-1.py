class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_so_far = 999999
        for price in prices:
            curr_profit = price - min_so_far
            if curr_profit > max_profit:
                max_profit = curr_profit
                continue
            if price < min_so_far:
                min_so_far = price
        return max_profit
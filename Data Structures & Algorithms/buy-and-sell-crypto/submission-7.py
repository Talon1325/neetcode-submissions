class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        profit = 0
        for r in prices:
            if r < l:
                l = r
            if r - l > 0 and r - l > profit:
                profit = r - l
        return profit
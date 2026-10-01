class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        valley = 100
        for i in range(len(prices)-1):
            if prices[i] < valley:
                valley = prices[i]
            if prices[i] < prices[i+1] and prices[i+1] - valley > max:
                max = prices[i+1] - valley
            
        return max
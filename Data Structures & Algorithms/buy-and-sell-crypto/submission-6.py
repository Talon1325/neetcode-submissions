class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        sum = 0
        while r <= len(prices)-1:
            if r == l:
                r += 1
                continue
            if prices[l] < prices[r]:
                sum = max(sum, prices[r] - prices[l])
                r += 1
            else:
                l += 1
            
        return sum
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        output = 0
        while r < len(prices) - 1:
            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
            output = max(output, prices[r] - prices[l])
            print(output, l, r)

        return output
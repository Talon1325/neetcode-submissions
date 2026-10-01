class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costD = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            costD[i] = min(costD[i-1] + cost[i-1], costD[i-2] + cost[i-2])
        return costD[len(cost)]
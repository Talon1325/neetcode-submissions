class Solution:
    def climbStairs(self, n: int) -> int:
        target = 1
        prev = target
        for i in range(1,n):
            target += prev
            prev = target - prev

        return target
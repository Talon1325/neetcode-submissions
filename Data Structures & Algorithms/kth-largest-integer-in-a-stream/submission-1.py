class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        self.res = [None]

    def add(self, val: int) -> int:
        max = 0
        self.nums.append(val)
        self.nums = sorted(self.nums)
        for i in range(1,self.k+1):
            max = self.nums[-(i)]
            print(self.nums[-(i)])
        return max

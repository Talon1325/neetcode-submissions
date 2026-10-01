class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        j = 0
        arr = []
        for i in range(len(nums)-k+1):
            max = -100000
            for i in range(j,k):
                if nums[i] > max:
                    max = nums[i]
            j += 1
            k += 1
            arr.append(max)
        return arr
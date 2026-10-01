class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = nums
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums:
                idx = nums.index(difference)
                if idx != i:
                    return sorted([i, idx])
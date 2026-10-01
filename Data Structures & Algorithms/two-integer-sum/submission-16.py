class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[i] in ans:
                return [nums.index(target - nums[i]),i]
            ans.append(target - nums[i])
        return []

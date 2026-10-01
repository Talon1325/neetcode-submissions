class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = set(nums)
        nums = sorted(nums)
        if len(nums) == 1:
            return 1
        
        longest = []
        count = 1
        for start in range(1, len(nums)):
            if nums[start - 1] == nums[start] - 1:
                count += 1
            else:
                longest.append(count)
                count = 1
        longest.append(count)

        return max(longest)
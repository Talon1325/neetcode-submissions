class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        matching = set()
        for i in nums:
            matching.add(i)
        if len(matching) == len(nums):
            return False
        return True
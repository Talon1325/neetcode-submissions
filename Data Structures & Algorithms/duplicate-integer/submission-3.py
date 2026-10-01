class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupCheck = set(nums)
        if len(nums) == len(dupCheck):
            return False
        return True
        
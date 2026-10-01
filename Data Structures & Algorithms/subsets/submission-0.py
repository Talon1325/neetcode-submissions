class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == None:
            return [[]]
        subset = []
        res = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return res
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res



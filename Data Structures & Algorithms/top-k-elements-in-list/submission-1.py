class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mynums = {}
        sol = []
        for i in nums:
            mynums[i] = 0
        for i in nums:
            mynums[i] += 1
            
        sortnums = dict(sorted(mynums.items(), key=lambda item: item[1], reverse = True))

        for i in range(k):
            sol.append(list(sortnums)[i])

        return sol
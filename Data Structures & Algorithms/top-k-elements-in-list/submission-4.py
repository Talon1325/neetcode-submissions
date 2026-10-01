class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mynums = {}
    
        for i in nums:
            mynums[i] = 0
        for i in nums:
            mynums[i] += 1

        bucket = [[] for i in range(len(nums)+ 1)]
        for num, freq in mynums.items():
            bucket[freq].append(num)
        
        sol = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                sol.append(num)
                if len(sol) == k:
                    return sol
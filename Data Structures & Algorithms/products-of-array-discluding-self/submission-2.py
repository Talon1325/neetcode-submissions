class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        presum = []
        firstsum = nums[0]
        presum.append(1)
        for i in range(1, len(nums)):
            presum.append(firstsum)
            firstsum *= nums[i]
        presum.append(firstsum)

        
        sufsum = []
        lastsum = nums[len(nums)-1]
        for i in range(len(nums) - 2, -1, -1):
            sufsum.append(lastsum)
            lastsum *= nums[i]
        sufsum.append(lastsum)

        sufsum = sufsum[::-1]
        sufsum.append(1)

        output = []
        for i in range(len(nums)):
            output.append(presum[i] * sufsum[i+1])

        return output
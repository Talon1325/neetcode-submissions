class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)


        for num in range(len(nums) - 2):
            if nums[num] > 0:
                break
            if num > 0 and nums[num] == nums[num - 1]:
                continue

            left = num + 1
            right = len(nums) - 1
            while left < right:
                total = nums[num] + nums[left] + nums[right]
    
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[num], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return ans
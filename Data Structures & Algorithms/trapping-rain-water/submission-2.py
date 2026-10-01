class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        output = 0
        left, right = 0, len(height) - 1
        maxL = height[left]
        maxR = height[right]

        while left < right:

            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                output += maxL - height[left]

            else:
                right -= 1
                maxR = max(maxR, height[right])
                output += maxR - height[right]
        
        return output
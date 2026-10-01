class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        curr = 0
        length = 0
        for i in range(len(heights)):
            length = 0
            for j in range(i+1,len(heights)):
                length += 1
                if heights[i] < heights[j]:
                    curr = heights[i]*length
                elif heights[j] < heights[i]:
                    curr = heights[j]*length
                else:
                    curr = heights[j]*length
                print(curr,length)
                if curr > max:
                    max = curr
        return max
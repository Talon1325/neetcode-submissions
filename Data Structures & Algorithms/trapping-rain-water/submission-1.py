class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        left = 0
        right = len(height) - 1

        maxL = []
        maxl = 0
        for l in height:
            maxL.append(maxl)
            maxl = max(maxl, l)
            

        maxR = []
        maxr = 0
        for r in height[::-1]:
            maxR.append(maxr)
            maxr = max(maxr, r)
        maxR = maxR[::-1]    

        for i in range(len(height)):
            if min(maxL[i], maxR[i]) - height[i] > 0:
                output  += min(maxL[i], maxR[i]) - height[i]

        return output


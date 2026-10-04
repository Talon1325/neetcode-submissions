class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1) - 1
        counts1 = {}
        
        l = 0
        for i in range(len(s1)):
            counts1[s1[i]] = 1 + counts1.get(s1[i], 0)
        
        for r in range(length, len(s2)):
            counts2 = {}
            for i in range(l, r + 1):
                counts2[s2[i]] = 1 + counts2.get(s2[i], 0)
            if counts2 == counts1:
                return True
            l += 1
        return False
        
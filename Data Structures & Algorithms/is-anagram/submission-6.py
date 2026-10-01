class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        tmap = [0] * 26
        smap = [0] * 26
        
        for c in s:
            smap[ord(c) - ord('a')] += 1
        for c in t:
            tmap[ord(c) - ord('a')] += 1

        for i in range(len(tmap)):
            if tmap[i] != smap[i]:
                return False
        
        return True
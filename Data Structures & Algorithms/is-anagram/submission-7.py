class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        tmap = [0] * 26
        smap = [0] * 26
        
        for c in range(len(s)):
            smap[ord(s[c]) - ord('a')] += 1
            tmap[ord(t[c]) - ord('a')] += 1

        for i in range(len(tmap)):
            if tmap[i] != smap[i]:
                return False
        
        return True
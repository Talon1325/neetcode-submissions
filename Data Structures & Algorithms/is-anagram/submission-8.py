class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = [0]*26
        countT = [0]*26
        for i in s:
            countS[ord(i)-ord("a")] += 1
        for i in t:
            countT[ord(i)-ord("a")] += 1
        if countT == countS:
            return True
        return False
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newS = ""
        count = 0
        max = 0
        for strs in s:
            if strs in newS:
                newS = newS[newS.index(strs) + 1:]
                count = len(newS)
            newS += strs
            count += 1
            if count > max:
                max = count
        return max
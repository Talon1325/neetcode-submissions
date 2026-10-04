class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        l, r = 0, 0
        longest = 1
        while r < len(s) - 1:
            if s[r + 1] in s[l:r+1]: 
                l += 1
                r -= 1
            r += 1
            longest = max(longest, len(s[l:r+1]))

    
        return longest
        
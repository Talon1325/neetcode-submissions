class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l < r:
            if not s[l].isalnum() or s[l] == ' ':
                l += 1
                continue
            if not s[r].isalnum() or s[r] == ' ':
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

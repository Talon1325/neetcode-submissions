class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join([char.lower() for char in s if char.isalnum()])

        if cleaned[:len(cleaned)//2+1] == cleaned[len(cleaned)//2 : len(cleaned)][::-1] and len(cleaned) % 2 == 1:
            return True
        if cleaned[:len(cleaned)//2] == cleaned[len(cleaned)//2 : len(cleaned)][::-1]:
            return True
        return False

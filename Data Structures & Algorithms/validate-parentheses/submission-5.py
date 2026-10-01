class Solution:
    def isValid(self, s: str) -> bool:
        present = {")" : "(","]" : "[","}" : "{"}
        stack = []
        for c in s:
            if c in present:
                if stack and stack[-1] == present[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)


        return True if not stack else False
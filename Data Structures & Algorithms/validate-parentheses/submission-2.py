class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        RandomDic = { ")" : "(","]" : "[" , "}" : "{"}
        for i in s:
            if i in RandomDic:
                if stack and stack[-1] == RandomDic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        
        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                num, index = stack.pop()
                result[index] = i - index
            stack.append((n,i))

        return result
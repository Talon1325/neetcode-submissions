# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Implementation of insertionsort on a list of pairs
        n = len(pairs)
        res = [] # The array with all iterations of insertions

        for i in range(n):
            j = i - 1 

            while j >= 0 and pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1

            res.append(pairs[:])
        return res

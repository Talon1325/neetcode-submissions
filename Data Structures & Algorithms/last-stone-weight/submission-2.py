class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if stones == None:
            return 0

        maxHeap = []
        for i in stones:
            heapq.heappush(maxHeap, -(i))
        while len(maxHeap) > 1:
            one = heapq.heappop(maxHeap)
            two = heapq.heappop(maxHeap)

            if one == two:
                continue
            elif one < two:
                heapq.heappush(maxHeap, one - two)
            elif two < one:
                heapq.heappush(maxHeap, two - one)

        if maxHeap == []:
            return 0
        return -(maxHeap[0])
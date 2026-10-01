class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.Heap, self.k = nums, k
        heapq.heapify(self.Heap)
        while len(self.Heap) > k:
            heapq.heappop(self.Heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.Heap, val)
        while len(self.Heap) > self.k:
            heapq.heappop(self.Heap)
        return self.Heap[0]

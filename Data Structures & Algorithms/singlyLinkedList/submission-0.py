class LinkedList:
    
    def __init__(self):
        self.arr = []
        self.length = 0
    
    def get(self, index: int) -> int:
        if index < len(self.arr):
            return self.arr[index]
        return -1

    def insertHead(self, val: int) -> None:
        self.arr = self.arr + [0]
        self.length += 1
        for i in range(len(self.arr)-1):
	        self.arr[len(self.arr)-1 - i] = self.arr[len(self.arr)-1 - i-1]
        self.arr[0] = val

    def insertTail(self, val: int) -> None:
        self.arr = self.arr + [0]
        self.length += 1
        self.arr[len(self.arr)-1] = val

    def remove(self, index: int) -> bool:
        if index < len(self.arr):
            self.arr.pop(index)
            return True
        return False

    def getValues(self) -> List[int]:
        return self.arr

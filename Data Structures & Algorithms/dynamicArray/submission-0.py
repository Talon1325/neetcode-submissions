class DynamicArray:

    length = 0
    arrcapacity = 0
    arr = []
    def __init__(self, capacity: int):
        self.arrcapacity = capacity
        self.arr = [None] * self.arrcapacity
        self.length = 0
        

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        return None

    def pushback(self, n: int) -> None:
        if(self.length == self.arrcapacity):
            self.resize()
        self.arr[self.length] = n
        self.length += 1
        return None

    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]
 

    def resize(self) -> None:
        self.arr = self.arr + [None] * self.arrcapacity
        self.arrcapacity = 2*self.arrcapacity
        return None

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.arrcapacity

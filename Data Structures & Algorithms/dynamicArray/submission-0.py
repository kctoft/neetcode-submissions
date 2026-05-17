class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        # return the element at position i of the array
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        # set the element at index i to the value n
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        # push the element n to the end of the array
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        # pop and return the element at the end of the array
        self.length -= 1 # soft delete
        return self.arr[self.length]


    def resize(self) -> None:
        # doubles the capacity of the array
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


    def getSize(self) -> int:
        # returns the number of elements in array
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity

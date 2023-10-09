class DynamicArray:

    def __init__(self, capacity):

        """ DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0. """

        self.size = 0
        self.arr = [None] * capacity

    
    def get(self,i):

        """ int get(int i) will return the element at index i. Assume that index i is valid. """

        return self.arr[i]

    def set(self,i,n):

        """ void set(int i, int n) will set the element at index i to n. Assume that index i is valid. """

        self.size = max(i+1, self.size)
        while (self.size > len(self.arr)):
            self.resize()
        
        self.arr[i] = n

    def pushback(self,n):

        """ void pushback(int n) will push the element n to the end of the array. """

        self.set(self.size,n)

    def popback(self,):

        """ int popback() will pop and return the element at the end of the array. Assume that the array is non-empty. """

        val, self.arr[self.size-1] = self.arr[self.size-1], None
        self.size -= 1
        return val

    def resize(self,):

        """ void resize() will double the capacity of the array. """

        self.arr += [None for _ in range(len(self.arr))]

    def getSize(self,):

        """ int getSize() will return the number of elements in the array. """

        return self.size

    def getCapacity(self,):

        """ int getCapacity() will return the capacity of the array. """

        return len(self.arr)

da = DynamicArray(1)

assert da.getSize() == 0, "Incorrect size: answer is 0 you returned " + str(da.getSize())
assert da.getCapacity() == 1, "Incorrect capacity: answer is 1 you returned "+ str(da.getCapacity())

da = DynamicArray(3)
da.pushback(0)
da.pushback(1)
da.pushback(2)
assert da.getSize() == 3, "Incorrect size: answer is 3 you returned " + str(da.getSize())
assert da.getCapacity() == 3, "Incorrect capacity: answer is 3 you returned "+ str(da.getCapacity())


class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.arr = [0] * self.capacity

    def print(self):
        for i in range(self.size):
            if i + 1 == self.size:
                print(self.arr[i])
            else:
                print(self.arr[i], end=", ")

    
    def prepend(self, value):
        if self.capacity <= self.size:
            self.resize()
        for i in range(self.size):
            self.arr[self.size - i] = self.arr[self.size - i - 1]
        self.arr[0] = value
        self.size += 1

    
    def insert(self, value, index):
        if index < value:
            if self.size >= self.capacity:
                self.resize()
            for i in range(self.size - index):
                self.arr[self.size - i] = self.arr[self.size - i - 1]
            self.arr[index] = value
            self.size += 1
        else:
            print("Index out of range")

    
    def append(self, value):
        if self.size >= self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    
    def set_at(self, value, index):
        self.arr[index] = value

    
    def get_first(self):
        if self.size == 0:
            raise Exception("Empty")
        return self.arr[0]


    def get_at(self, index):

        return self.arr[index]

    
    def get_last(self):
        if self.size == 0:
            raise Exception("Empty")
        return self.arr[self.size -1]

    
    def resize(self):
        self.capacity *= 2
        new_stack = (self.capacity) * [0]
        for i in range(self.size):
            new_stack[i] = self.arr[i]
        self.arr = new_stack

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        for i in range(self.size - index):
            self.arr[index + i] = self.arr[index + i + 1]
        self.size -= 1

    #Time complexity: O(1) - constant time
    def clear(self):
        self.size = 0

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n^2) - quadratic time in size of list
    #Time complexity: O(n log n) - linear times logarythmic time in size of list
    def sort(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

A = ArrayList()
A.append(4)
A.clear()
A.prepend(34)
A.prepend(33)
A.append(345)
A.print()
print(A.get_last())
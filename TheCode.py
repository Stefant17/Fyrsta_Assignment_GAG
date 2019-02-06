class Arraylist:
  def __init__(self):
    self.size = 0
    self.capacity = 4
    self.arr = [0] * self.capacity

  def print(self):
    for i in range(self.size):
      print(self.arr[i])

  def prepend(self, value):
    if(self.capacity <= self.size):
      resize()
    for i in range(self.size):
      self.arr[i] = self.arr[i+1]
    self.arr[0] = value
    return 0

def insert(self, value, index): 
  if((self.size / self.capacity) == 1):
    Arraylist = resize(self)
  for i in range(self.size): 
    if i >= index: 
      self.arr[i] = self.arr[i+1]
  self.arr[index] = value
  self.size += 1
  print(self.arr)


  def append(self, value):
    if (self.capacity < self.size):
      resize(self)
    self.arr[self.size] = value
    return 0

  def set_at(self, value, index):
    if(index > self.capacity or index < 0):
      return 0 
    self.arr[index] = value

  def get_first(self):
    if self.size == 0: 
      raise Empty()
    return self.arr[0]

  def get_last(self): 
    if self.size == 0: 
      raise Empty()
    return self.arr[self.size-1]

  def resize(self):
    array = [0] * (self.capacity * 2)
    for i in range(self.size): 
      self.arr[i] = array.arr[i]
    self.arr = array
    return self

  def remove_at(self, index):
    for i in range(self.size, -1, -1):
      return 0

  def clear(self):
    for i in range(self.size):
      self.arr[i] = 0
  
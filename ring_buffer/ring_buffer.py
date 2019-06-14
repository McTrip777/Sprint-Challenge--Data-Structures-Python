class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < self.capacity:
      del self.storage[self.current]
      self.storage.insert(self.current, item)
      self.current += 1
    elif self.current == self.capacity:
      self.current = 0
      del self.storage[self.current]
      self.storage.insert(self.current, item)
      self.current += 1
      
  def get(self):
    list = []
    for i in self.storage:
      if i is not None:
        list.append(i)
    return list 


r = RingBuffer(11)
r.append(1)
r.append(2)
r.append(3)
r.append(4)
r.append(5)

r.get()
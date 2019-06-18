class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # first check the current index against capacity to whether to reset current index to zero
    if self.current == self.capacity:
      self.current = 0
    # overwrite and add current item
    self.storage[self.current] = item
    self.current += 1

  def get(self):
    # initiate a list and iterate through ring buffer
    elements = []
    for i in range(self.capacity):
      if self.storage[i]:
        elements += self.storage[i]
    return elements
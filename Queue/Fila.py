class Fila:
    def __init__(self):
        self.items = []

     
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self , item):
      for i in range(0,2):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.items)





    
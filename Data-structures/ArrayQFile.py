from array import array
# i den här labben ska vi lagra integers

class ArrayQ:
    def __init__(self):
        self.queue = array("i")

    def __str__(self):
        return str(self.queue)
    
    def size(self):
        x = len(self.queue)
        return x
    
    def enqueue(self,x):
        self.queue.append(x)
        return
    
    def dequeue(self):
        x = self.queue.pop(0)
        return x 
    
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
 
    



class Node:
    def __init__(self, indata):
        self.data = indata
        self.next = None

    def __str__(self):
        return self.data
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        if self.size() == 0:
            return ''
        else:
            tempString = str() #skapar en sträng för att returnera
            if self.first == None:
                return None #ifall den är tom returnera None
            else:
                
                temp=self.first
                for x in range(self.size()):    #går igenom listan och adderar till tempString
                
                    tempString += temp.data
                    temp=temp.getNext()
                return tempString

    

    def enqueue(self, newItem):

        if self.isEmpty()==True:    #om tom skapar ny nod och sätter first = last
            self.first = Node(newItem)
            self.last = self.first
        
        else:                       
            newNode = Node(newItem) # gör ny nod av indatan
            self.last.setNext(newNode) #går längst bak i listan o sätter nästa till nya noden
            self.last = newNode #uppdaterar sista noden

        
    def dequeue(self):

        outNode = self.last#det som vi tar bort från 

        if self.size() > 1:
             
            outNode = self.first    #först i kön
            self.first = self.first.getNext()   #uppdaterar den första noden

        elif self.size()==1:
            outNode = self.first    #om den är tom returnerar noden och sätter både först o sist till None
            self.first=None
            self.last=None

        else:
            print("listan är tom")  

        return outNode.getData()


        
    def isEmpty(self):
        return self.first == None
    
    def size(self): 
        current = self.first
        count = 0
        while current != None:  #räjnar igenom listan tills vi pekar på None och räknar via en count
            count = count + 1
            current = current.getNext()
        return count
    
    def peek(self):
        return  self.first.getData()
        

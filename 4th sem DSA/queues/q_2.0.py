class Queue:
    def __init__(self,limit):
        self.limit = limit
        self.Q=[]
        self.size=0
    def enqueue(self,data):
        if self.size == self.limit:
            return "overflow"
        else:
            self.Q.append(data)
            self.size += 1
                
    def dequeue(self):
        if self.size == 0:
            return "underflow"
        else:
            self.Q.pop(0)
            self.size -=1
    def isfull(self):
        return self.size == self.limit
            
    def isempty(self):
        return self.size == 0

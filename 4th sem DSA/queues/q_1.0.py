class Queue:
    def __init__(self,size):
        self.Q=[]
        self.size=size
    def isempty(self):
        return self.Q==[]
    def isfull(self):
        return len(self.Q)==self.size
    def enqueue(self,data):
        if self.isfull():
            return "overflow"
        else:
            self.Q.append(data)
    def dequeue(self):
        if self.isempty():
            return "underflow"
        else:
            self.Q.pop(0)
    def print(self):
        return self.Q 
    
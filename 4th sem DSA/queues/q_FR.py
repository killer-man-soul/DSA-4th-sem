class Queue:
    def __init__(self,limit):
        self.limit = limit
        self.front = self.rear = -1
        self.Q=[]

    def enqueue(self,data):
        if self.rear == self.limit-1:
            return "overflow"
        else:
            self.Q.append(data)
            if self.front == -1 and self.rear == -1:
                self.front+=1
                self.rear+=1
            else:
                self.rear+=1
                            
    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            return "underflow"
        else:
            self.Q.pop(0)
            if self.front == 0 and self.rear == 0:
                self.front -=1
                self.rear -=1
            else:
                self.front +=1

    def display(self):
        return self.Q
    
    def front_(self):
        if self.isempty():
            print("queue is empty")
        else :
            return self.Q[self.front]

    def rear_(self):
        if self.isempty():
            print("ques is empty")
        else:
            return self.Q[self.rear]
            
    def isfull(self):
        return self.rear == self.limit-1
    
    def isempty(self):
        return self.front == self.rear

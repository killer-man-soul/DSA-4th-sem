class Queue:
    def _init_(self):
        self.elements = []
        self.f=-1
        self.r=-1
        self.n = int(input("Enter size of queue:"))
    def enqueue(self,item):
        if((self.f==self.r+1) or ((self.f==0) and (self.r==self.n-1))):
            return "queue overflow"
        else:
            if((self.r==-1) and (self.f==-1)):
                self.f=(self.f+1)%self.n
                self.r=(self.r+1)%self.n
                self.elements.append(item)
                return self.elements
            else:
                self.r=(self.r+1)%self.n
                self.elements.insert(self.r,item)
                return self.elements
    def dequeue(self):
        if((self.f==-1) and (self.r==-1)):
            return "queue underflow"
        else:
            if((self.f==self.r)):
                item=self.elements.pop(0)
                self.f=-1
                self.r=-1
                return item
            else:
                item=self.elements.pop(0)
                self.f=(self.f+1)%self.n

                return item
    def isfull(self):
        if((self.f==self.r+1) or ((self.f==0) and (self.r==self.n-1))):
            return "queue is full"
        else:
            return self.elements
    def isempty(self):
        if((self.f==-1) and (self.r==-1)):
            return "Queue is empty"
        else:
            return self.elements
    def length(self):
        return len(self.elements)
    def display(self):
        return self.elements
    def display1(self):
        return self.r

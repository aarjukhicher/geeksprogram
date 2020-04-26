class Queue:
    def __init__(self):
        self.queue_l = []
    def push_el(self,data):
        self.queue_l.append(data)
        return
    def reversequ(self):
        qlen =len(self.queue_l)-1
        k = 0
        temp = None
        while(qlen>k):
            temp = self.queue_l[qlen]
            self.queue_l[qlen] = self.queue_l[k]
            self.queue_l[k] = temp
            qlen = qlen-1
            k = k+1
    def printqueue(self):
        qlen = len(self.queue_l)
        for k in range(qlen):
            print(self.queue_l[k])
    
if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        qu = Queue()
        n = int(input("n "))
        for j in range(n):
            qu.push_el(input("input "))
        qu.reversequ()
        qu.printqueue()
        
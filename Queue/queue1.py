class Queue:
    def __init__(self):
        self.queue_l = []
    
    def push_el(self,data):
        self.queue_l.append(data)
        return
    def pop_el(self):
        temp = self.queue_l.pop(0)
        print("poped data is ",temp)
        return

    def printqueue(self):
        queuelen = len(self.queue_l)
        for k in range(queuelen):
            print(self.queue_l[k])
    
if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        qu = Queue()
        n = int(input("n "))
        for j in range(n):
            qu.push_el(input("input "))
        qu.printqueue()
        qu.pop_el()
        qu.printqueue()
    
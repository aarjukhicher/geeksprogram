class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insertlist(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def getcount(self):
        count = 0
        test = self.head
        while(test):
            count = count + 1
            test = test.next
        if count % 2 == 0:
            print("EVEN NODES")
        else:
            print("ODD NODES")
    
if __name__=="__main__":
    t = int(input("t  "))
    for i in range(t):
        llist = Linkedlist()
        n = int(input("n  "))
        for j in range(n):
            llist.insertlist(input("value "))
        llist.getcount()
        llist.printlist()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insertlist(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printlist(self):
        test = self.head
        while test:
            print(test.data)
            test = test.next

    def getmid(self):
        temp = self.head
        mid = None
        count = 0
        if temp == None:
            print("no mid element")
            return
        while temp != None:
            count += 1
            temp = temp.next
        count = int(count/2)
        mid = self.head
        while(count > 0):
            count = count-1
            mid = mid.next
        print("mid element ",mid.data)
    
if __name__=="__main__":
    llist = Linkedlist()
    n = int(input("n "))
    for i in range(n):
        llist.insertlist(input("input "))
    llist.printlist()
    llist.getmid()

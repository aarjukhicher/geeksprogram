class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insertnode(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
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
    def insertmid(self,key):
        mid =int(n/2)
        print("mid ",mid)
        test = self.head
        while(mid>1):
            test = test.next
            mid = mid-1
        print("test node ",test.data)
        new_node = Node(key)
        print("temp1 ",new_node.data)
        new_node.next = test.next
        test.next = new_node

if __name__=="__main__":
    llist = Linkedlist()
    n =int(input("n "))
    for i in range(n):
        llist.insertnode(input("input "))
    llist.insertmid(input("mid key "))
    print("new node is ")
    llist.printlist()

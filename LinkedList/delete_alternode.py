class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insertnode(self,new_data):
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
    
    def delete_alter(self):
        prev = self.head
        test = prev.next
        while(prev != None and test != None):
            prev.next = test.next
            test = None
            prev = prev.next
            if prev != None:
                test = prev.next

if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        llist = Linkedlist()
        n = int(input("n "))
        for j in range(n):
            llist.insertnode(input("N "))
        llist.delete_alter()
        llist.printlist()
        
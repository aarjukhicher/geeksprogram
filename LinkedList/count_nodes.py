class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert_node(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getcounts(self):
        temp = self.head
        count = 0
        while(temp is not None):
            count = count+1
            temp = temp.next
        print("number of nodes are  : ",count)

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=="__main__":
    t = int(input("number of test cases "))
    for i in range(t):
        llist = Linkedlist()
        n = int(input("number of inputs "))
        for j in range(n):
            llist.insert_node(input("Node "))
        
        llist.printlist()
        llist.getcounts()

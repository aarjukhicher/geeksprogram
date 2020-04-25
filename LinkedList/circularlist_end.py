class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CLinkedlist:
    def __init__(self):
        self.head = None
    def insertend(self,new_data):
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            self.head.next = self.head

        new_node.next = self.head.next
        self.head.next = new_node
        self.head = new_node
    def printlist(self):
        test = self.head
        while(test != None):
            print(test.data)
            test = test.next
            if test == self.head:
                return
    
if __name__=="__main__":
    clist = CLinkedlist()
    clist.insertend(input("input "))
    clist.insertend(input("input "))
    clist.printlist()

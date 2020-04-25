class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CLinkedlist:
    def __init__(self):
        self.head = None
    
    def insertlist(self,new_data):
        new_node = Node(new_data)
        temp = self.head

        new_node.next = self.head
        if self.head != None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node
    def printlist(self):
        test =self.head
        while(test != None):
            print(test.data)
            test = test.next
            if test == self.head:
                return
    
if __name__=="__main__":
    clist = CLinkedlist()
    n = int(input("n "))
    for i in range(n):
        clist.insertlist(input("input "))
    clist.printlist()
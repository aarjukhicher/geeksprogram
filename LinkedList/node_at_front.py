class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def node_at_front(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=="__main__":
    llist = Linkedlist()

    llist.head = Node(1)
    llist.node_at_front(2)
    llist.printlist()

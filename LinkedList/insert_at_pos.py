class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at(self,pre_node,new_data):
        if pre_node is None:
            print("wrong node given")
            return
        new_node = Node(new_data)
        new_node.next = pre_node.next
        pre_node.next = new_node
    
    def printlist(self):
        temp = self.head

        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=="__main__":
    llist = Linkedlist()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    llist.head.next = second
    second.next = third
    third.next = fourth

    llist.insert_at(second,5)
    llist.printlist()

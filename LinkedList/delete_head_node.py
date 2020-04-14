class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def delete_node(self):
        temp = self.head
        if temp is None:
            print("node is empty")
        else:
            self.head = temp.next
            temp = None
            return


if __name__=="__main__":
    llist = Linkedlist()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    llist.head.next = second
    second.next = third
    third.next = fourth

    llist.printlist()
    llist.delete_node()
    llist.printlist()

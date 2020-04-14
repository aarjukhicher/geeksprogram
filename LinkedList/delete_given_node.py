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
    def delete_node(self,key):
        temp = self.head
        if(temp == None):
            print("list is empty ")
            return
        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            print("prev and temp",prev.data,temp.data)
            temp = temp.next
        prev.next = temp.next
        temp = None

if __name__=="__main__":
    llist = Linkedlist()

    llist.head = Node(1)
    sec = Node(2)
    thir = Node(3)
    fourt = Node(4)

    llist.head.next = sec
    sec.next = thir
    thir.next = fourt

    llist.printlist()
    llist.delete_node(3)
    llist.printlist()
        
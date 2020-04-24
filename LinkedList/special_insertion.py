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
    def insertatend(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
    def insertathead(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
if __name__=="__main__":
    llist = Linkedlist()
    n = int(input("number of nodes "))
    a = []
    for i in range(2*n):
        a.append(input("enter value and situation "))
    print("a values are : ",a)
    for j in range(2*n):
        if j%2 == 0:
            if a[j+1] == "0" :
                llist.insertathead(a[j])
            else :
                llist.insertatend(a[j])
    llist.printlist()
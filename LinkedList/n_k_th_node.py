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
    def k_thelement(self):
        test =self.head
        kth = n/k
        if kth%1 == 0:
            kth = int(kth)
            while(kth>1):
                test = test.next
                kth = kth - 1
        else:
            kth = int(kth)
            while(kth>0):
                test = test.next
                kth = kth - 1
        print("kth element is ",test.data)
if __name__=="__main__":
    llist = Linkedlist()
    n = int(input("n "))
    for i in range(n):
        llist.insertnode(input("input node value "))
    llist.printlist()
    k = int(input("k_th value and "))
    llist.k_thelement()


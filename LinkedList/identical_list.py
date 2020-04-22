class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def identical(self,li):
        l1 = self.head
        l2 = li.head
        match = 1
        while(l1 !=None and l2 !=None):
            print("l1 ",l1.data)
            print("l2 ",l2.data)
            if l1.data == l2.data :
                match = 0
            else:
                match = 1
                return print(match)
            l1 = l1.next
            l2 = l2.next
        if l1 == None and l2 == None:
            match = 0
            print(match)
        else:
            print(match)
    
    def insertlist(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node

    def printlist(self):
        test = self.head
        while(test):
            print(test.data)
            test = test.next

if __name__=="__main__":
        llist = Linkedlist()
        llist1 = Linkedlist()
        n = int(input("n "))
        for j in range(n):
            llist.insertlist(input("input for list1 "))
            llist1.insertlist(input("input for list2 "))
        llist.identical(llist1)

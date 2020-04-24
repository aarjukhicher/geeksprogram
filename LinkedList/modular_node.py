class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def insertnode(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def modularnode(self):
        test = self.head
        modenode = -1
        i = 1
        while(i<=n):
            if i%k == 0:
                modenode = test.data
            test = test.next
            i = i+1
        print(modenode)

    
if __name__=="__main__":
    llist = Linkedlist()
    n = int(input("n "))
    for i in range(n):
        llist.insertnode(int(input("input ")))
    k = int(input("k "))
    llist.modularnode()
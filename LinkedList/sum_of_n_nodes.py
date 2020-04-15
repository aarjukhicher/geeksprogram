class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkiedlist:
    def __init__(self):
        self.head = None
    def insertnode(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node
    
    def getsum(self):
        temp = self.head
        sum_n = 0
        for k in range(N):
            sum_n = sum_n + temp.data
            temp = temp.next
        print("sum of N nodes ",sum_n)
    
if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        llist = Linkiedlist()
        n = int(input("n "))
        N = int(input("N "))
        for j in range(n):
            llist.insertnode(int(input()))
        llist.getsum()


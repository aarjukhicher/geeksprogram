class Stack:
    def __init__(self):
        self.stack_s = []
    def pushstack(self,data):
        self.stack_s.append(data)
        return
    def popstack(self):
        while(self.stack_s != None):
            print(self.stack_s.pop())
    
if __name__=="__main__":
    t = int(input("t "))
    for i in range(t):
        st = Stack()
        n = int(input("n "))
        for j in range(n):
            st.pushstack(input("input "))
        st.popstack()

class Stack:
    def __init__(self):
        self.stack_s = []
    def pushstack(self,data):
        self.stack_s.append(data)
        return
    def popstack(self):
        temp = None
        if self.stack_s == None or self.stack_s[len(self.stack_s)-1] == -1:
            self.stack_s.append(-1)
            return
        temp = self.stack_s.pop()
        print("poped item is ",temp)
    def printstack(self):
        stack_len = len(self.stack_s)
        for i in range(stack_len):
            print(self.stack_s[i])

if __name__=="__main__":
    t = int(input("t "))
    for j in range(t):
        st = Stack()
        arr = []
        n = int(input("n "))
        k=0
        while(n > k):
            arr.append(input("input "))
            print("arr",arr)
            if arr[k] == 1:
                n = n+1
            else:
                pass
            k = k+1
            
        print("final value of n is : ",n)
        for k in range(n):
            if arr[k]== 1:
                k = k+1
                st.pushstack(arr[k])
            else:
                st.popstack()
        st.printstack()
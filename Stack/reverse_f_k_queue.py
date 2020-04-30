def insertqueue(n,data):
    queue.append(data)
def reverse_k(k):
    stack = []
    for i in range(k):
        stack.append(0)
        stack[i] = queue[i]
    print ("stack ",stack)
    
    for i in range(k):
        queue[i] =stack.pop()
    
if __name__=="__main__":
    t = int(input("t "))
    for t in range(t):
        queue = []
        n =int(input("n "))
        k = int(input("k "))
        for i in range(n):
            insertqueue(n,input("insert "))
        reverse_k(k)
        print(queue)
    